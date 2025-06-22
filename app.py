from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from datetime import datetime
import folium
import os
from dotenv import load_dotenv
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from admin_users import ADMINS

app = Flask(__name__, template_folder='templates')
load_dotenv()

app.secret_key = os.environ.get('SECRET_KEY', 'chave')
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

class AdminUser(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in ADMINS:
        return AdminUser(user_id)
    return None

def formatar_data(data_str):
    # Espera data no formato 'YYYY-MM-DD'
    try:
        return datetime.strptime(data_str, '%Y-%m-%d').strftime('%d/%m/%Y')
    except Exception:
        return data_str or ''

@app.route('/')
def index():
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()

    # Busca campanhas
    cursor.execute("SELECT * FROM VCCTB003_CAMPANHA_VACINACAO")
    campanhas = []
    for row in cursor.fetchall():
        # row[4] = DT_INICIO, row[5] = DT_FIM
        campanha = list(row)
        campanha[4] = formatar_data(campanha[4])
        campanha[5] = formatar_data(campanha[5])
        campanhas.append(campanha)

    # Busca vacinas e seus públicos alvo
    cursor.execute("""
        SELECT v.*, 
               GROUP_CONCAT(p.NO_PUBLICO_ALVO, ', ') as publicos
        FROM VCCTB002_VACINA v
        LEFT JOIN VCCTB006_VACINA_PUBLICO_ALVO vpa ON v.ID_VACINA = vpa.ID_VACINA
        LEFT JOIN VCCTB004_PUBLICO_ALVO p ON vpa.ID_PUBLICO_ALVO = p.ID_PUBLICO_ALVO
        GROUP BY v.ID_VACINA
    """)
    vacinas = cursor.fetchall()

    conn.close()
    return render_template('index.html', campanhas=campanhas, vacinas=vacinas, now=datetime.now())

@app.route('/busca', methods=['GET'])
def busca():
    import sqlite3
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID_VACINA, NO_VACINA FROM VCCTB002_VACINA")
    vacinas = cursor.fetchall()
    cursor.execute("SELECT ID_POSTO, NO_POSTO, NR_LATITUDE, NR_LONGITUDE FROM VCCTB001_POSTO")
    postos = cursor.fetchall()

    resultado = None
    posto_lat = None
    posto_lng = None
    vacina_id = request.args.get('vacina')
    posto_id = request.args.get('localizacao')

    if vacina_id and posto_id:
        cursor.execute("""
            SELECT p.NO_POSTO, p.ED_POSTO, s.QT_DISPONIVEL, s.IC_STATUS, p.NR_LATITUDE, p.NR_LONGITUDE
            FROM VCCTB009_SALDO_ESTOQUE s
            JOIN VCCTB001_POSTO p ON s.ID_POSTO = p.ID_POSTO
            WHERE s.ID_POSTO = ? AND s.ID_VACINA = ?
        """, (posto_id, vacina_id))
        resultado = cursor.fetchone()
        if resultado:
            posto_lat = resultado[4]
            posto_lng = resultado[5]
    conn.close()
    from datetime import datetime
    return render_template(
        'busca.html',
        vacinas=vacinas,
        postos=postos,
        resultado=resultado,
        posto_lat=posto_lat,
        posto_lng=posto_lng,
        now=datetime.now(),
        google_maps_api_key=GOOGLE_MAPS_API_KEY
    )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', now=datetime.now())

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in ADMINS and ADMINS[username] == password:
            user = AdminUser(username)
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Usuário ou senha inválidos.')
    return render_template('admin_login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
def admin_dashboard():
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VCCTB001_POSTO")
    postos = cursor.fetchall()
    cursor.execute("SELECT * FROM VCCTB002_VACINA")
    vacinas = cursor.fetchall()
    cursor.execute("SELECT * FROM VCCTB009_SALDO_ESTOQUE")
    saldos = cursor.fetchall()
    conn.close()
    return render_template('admin_dashboard.html', postos=postos, vacinas=vacinas, saldos=saldos)

@app.route('/admin/posto/add', methods=['GET', 'POST'])
@login_required
def admin_add_posto():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        # ... outros campos ...
        conn = sqlite3.connect('vacina_certa.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO VCCTB001_POSTO (NO_POSTO, ED_POSTO, HR_ABERTURA, HR_FECHAMENTO, NO_REGIAO, NR_LONGITUDE, NR_LATITUDE) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nome, endereco, request.form['hr_abertura'], request.form['hr_fechamento'], request.form['regiao'], request.form['longitude'], request.form['latitude']))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_add_posto.html')

@app.route('/admin/posto/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_posto(id):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("""
            UPDATE VCCTB001_POSTO
            SET NO_POSTO=?, ED_POSTO=?, HR_ABERTURA=?, HR_FECHAMENTO=?, NO_REGIAO=?, NR_LONGITUDE=?, NR_LATITUDE=?
            WHERE ID_POSTO=?
        """, (
            request.form['nome'],
            request.form['endereco'],
            request.form['hr_abertura'],
            request.form['hr_fechamento'],
            request.form['regiao'],
            request.form['longitude'],
            request.form['latitude'],
            id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("SELECT * FROM VCCTB001_POSTO WHERE ID_POSTO=?", (id,))
    posto = cursor.fetchone()
    conn.close()
    return render_template('admin_edit_posto.html', posto=posto)

@app.route('/admin/posto/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_delete_posto(id):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM VCCTB001_POSTO WHERE ID_POSTO=?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("SELECT * FROM VCCTB001_POSTO WHERE ID_POSTO=?", (id,))
    posto = cursor.fetchone()
    conn.close()
    return render_template('admin_delete_posto.html', posto=posto)

@app.route('/admin/vacina/add', methods=['GET', 'POST'])
@login_required
def admin_add_vacina():
    if request.method == 'POST':
        conn = sqlite3.connect('vacina_certa.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO VCCTB002_VACINA 
            (NO_VACINA, DT_FABRICACAO, DT_VENCIMENTO, DS_VACINA, NO_PRINCIPIO_ATIVO, IC_TIPO_DOSE, IC_TIPO_APLICACAO, IC_ATIVO, IC_ORIGEM, NR_DOSES_RECOMENDADAS, DS_RESTRICAO_USO, ID_FABRICANTE)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            request.form['nome'],
            request.form['dt_fabricacao'],
            request.form['dt_vencimento'],
            request.form['descricao'],
            request.form['principio_ativo'],
            request.form['tipo_dose'],
            request.form['tipo_aplicacao'],
            request.form['ativo'],
            request.form['origem'],
            request.form['doses'],
            request.form['restricao'],
            request.form['fabricante']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    # Buscar fabricantes para o select
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID_FABRICANTE, NO_FABRICANTE FROM VCCTB008_FABRICANTE")
    fabricantes = cursor.fetchall()
    conn.close()
    return render_template('admin_add_vacina.html', fabricantes=fabricantes)

@app.route('/admin/vacina/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_vacina(id):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("""
            UPDATE VCCTB002_VACINA
            SET NO_VACINA=?, DT_FABRICACAO=?, DT_VENCIMENTO=?, DS_VACINA=?, NO_PRINCIPIO_ATIVO=?, IC_TIPO_DOSE=?, IC_TIPO_APLICACAO=?, IC_ATIVO=?, IC_ORIGEM=?, NR_DOSES_RECOMENDADAS=?, DS_RESTRICAO_USO=?, ID_FABRICANTE=?
            WHERE ID_VACINA=?
        """, (
            request.form['nome'],
            request.form['dt_fabricacao'],
            request.form['dt_vencimento'],
            request.form['descricao'],
            request.form['principio_ativo'],
            request.form['tipo_dose'],
            request.form['tipo_aplicacao'],
            request.form['ativo'],
            request.form['origem'],
            request.form['doses'],
            request.form['restricao'],
            request.form['fabricante'],
            id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("SELECT * FROM VCCTB002_VACINA WHERE ID_VACINA=?", (id,))
    vacina = cursor.fetchone()
    cursor.execute("SELECT ID_FABRICANTE, NO_FABRICANTE FROM VCCTB008_FABRICANTE")
    fabricantes = cursor.fetchall()
    conn.close()
    return render_template('admin_edit_vacina.html', vacina=vacina, fabricantes=fabricantes)

@app.route('/admin/vacina/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_delete_vacina(id):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM VCCTB002_VACINA WHERE ID_VACINA=?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("SELECT * FROM VCCTB002_VACINA WHERE ID_VACINA=?", (id,))
    vacina = cursor.fetchone()
    conn.close()
    return render_template('admin_delete_vacina.html', vacina=vacina)

@app.route('/admin/saldo/add', methods=['GET', 'POST'])
@login_required
def admin_add_saldo():
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("SELECT 1 FROM VCCTB009_SALDO_ESTOQUE WHERE ID_POSTO=? AND ID_VACINA=?", (request.form['posto'], request.form['vacina']))
        if cursor.fetchone():
            flash('Já existe saldo cadastrado para este posto e vacina.')
            # Recarregue o formulário com os selects
            cursor.execute("SELECT ID_POSTO, NO_POSTO FROM VCCTB001_POSTO")
            postos = cursor.fetchall()
            cursor.execute("SELECT ID_VACINA, NO_VACINA FROM VCCTB002_VACINA")
            vacinas = cursor.fetchall()
            conn.close()
            return render_template('admin_add_saldo.html', postos=postos, vacinas=vacinas)

        cursor.execute("""
            INSERT INTO VCCTB009_SALDO_ESTOQUE
            (ID_POSTO, ID_VACINA, QT_DISPONIVEL, IC_STATUS, DT_ATUALIZACAO)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form['posto'],
            request.form['vacina'],
            request.form['quantidade'],
            request.form['status'],
            request.form['data']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("SELECT ID_POSTO, NO_POSTO FROM VCCTB001_POSTO")
    postos = cursor.fetchall()
    cursor.execute("SELECT ID_VACINA, NO_VACINA FROM VCCTB002_VACINA")
    vacinas = cursor.fetchall()
    conn.close()
    return render_template('admin_add_saldo.html', postos=postos, vacinas=vacinas)

@app.route('/admin/saldo/edit/<int:id_posto>/<int:id_vacina>', methods=['GET', 'POST'])
@login_required
def admin_edit_saldo(id_posto, id_vacina):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("""
            UPDATE VCCTB009_SALDO_ESTOQUE
            SET QT_DISPONIVEL=?, IC_STATUS=?, DT_ATUALIZACAO=?
            WHERE ID_POSTO=? AND ID_VACINA=?
        """, (
            request.form['quantidade'],
            request.form['status'],
            request.form['data'],
            id_posto,
            id_vacina
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("""
        SELECT s.*, p.NO_POSTO, v.NO_VACINA
        FROM VCCTB009_SALDO_ESTOQUE s
        JOIN VCCTB001_POSTO p ON s.ID_POSTO = p.ID_POSTO
        JOIN VCCTB002_VACINA v ON s.ID_VACINA = v.ID_VACINA
        WHERE s.ID_POSTO=? AND s.ID_VACINA=?
    """, (id_posto, id_vacina))
    saldo = cursor.fetchone()
    conn.close()
    return render_template('admin_edit_saldo.html', saldo=saldo)

@app.route('/admin/saldo/delete/<int:id_posto>/<int:id_vacina>', methods=['GET', 'POST'])
@login_required
def admin_delete_saldo(id_posto, id_vacina):
    conn = sqlite3.connect('vacina_certa.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM VCCTB009_SALDO_ESTOQUE WHERE ID_POSTO=? AND ID_VACINA=?", (id_posto, id_vacina))
        conn.commit()
        conn.close()
        return redirect(url_for('admin_dashboard'))
    cursor.execute("""
        SELECT s.*, p.NO_POSTO, v.NO_VACINA
        FROM VCCTB009_SALDO_ESTOQUE s
        JOIN VCCTB001_POSTO p ON s.ID_POSTO = p.ID_POSTO
        JOIN VCCTB002_VACINA v ON s.ID_VACINA = v.ID_VACINA
        WHERE s.ID_POSTO=? AND s.ID_VACINA=?
    """, (id_posto, id_vacina))
    saldo = cursor.fetchone()
    conn.close()
    return render_template('admin_delete_saldo.html', saldo=saldo)



if __name__ == '__main__':
    app.run(debug=True)