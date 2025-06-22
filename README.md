# Vacina Certa

**Vacina Certa** é uma plataforma web desenvolvida como projeto final da disciplina de Novas Tecnologias da Universidade Católica de Brasília (UCB). O objetivo é facilitar o acesso da população do Distrito Federal às informações sobre vacinação, promovendo transparência, eficiência e praticidade no acompanhamento da disponibilidade de vacinas nos postos de saúde.

---

## 📌 Objetivo

O Vacina Certa surgiu como resposta à dificuldade enfrentada por cidadãos para encontrar informações confiáveis sobre:

- Disponibilidade de vacinas;
- Localização dos postos de saúde;
- Campanhas de vacinação ativas;
- Esclarecimento de dúvidas frequentes.

A proposta é **centralizar e simplificar o acesso à informação**, promovendo confiança, agilidade e prevenção.

---

## ✨ Funcionalidades

- **Busca de Vacinas:** Permite ao usuário pesquisar vacinas disponíveis por tipo e região, exibindo informações detalhadas e status do estoque (Completo, Médio, Vazio).
- **Visualização de Postos:** Lista e localiza postos de vacinação, com endereço, horário de funcionamento e localização no mapa.
- **Dashboard Administrativo:** Área restrita para administradores, com autenticação, onde é possível gerenciar:
  - Cadastro, edição e exclusão de postos de saúde.
  - Cadastro, edição e exclusão de vacinas.
  - Controle de saldo de vacinas por posto (CRUD completo da tabela associativa).
  - Cadastro de fabricantes de vacinas.
- **Mapas Integrados:** Visualização dos postos no mapa e traçado de rotas via Google Maps.
- **Design Responsivo:** Interface moderna, responsiva e acessível, com uso de Bootstrap 5 e ícones temáticos.
- **Mensagens e Alertas:** Feedback visual para ações do usuário e mensagens de sucesso/erro.
- **Página institucional** com perguntas frequentes (FAQ) e “Quem Somos”.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Flask, Flask-Login, SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript, Bootstrap Icons
- **APIs:** Google Maps API
- **Outros:** dotenv para variáveis de ambiente

---

## 📋 Requisitos

### Funcionais

- Permitir ao usuário pesquisar vacinas por nome, tipo e região.
- Exibir lista de postos de vacinação com informações detalhadas.
- Permitir ao administrador cadastrar, editar e excluir vacinas, postos e fabricantes.
- Permitir ao administrador gerenciar o saldo de vacinas por posto.
- Autenticação obrigatória para acesso ao painel administrativo.
- Exibir status do estoque de vacinas de forma visual e intuitiva.
- Permitir visualização dos postos em mapa integrado.
- Exibição de campanhas em destaque na página inicial.
- Área informativa com perguntas e respostas frequentes.

### Não Funcionais

- Interface responsiva e compatível com dispositivos móveis.
- Utilização de banco de dados SQLite para persistência dos dados.
- Segurança no acesso ao painel administrativo (Flask-Login).
- Feedback visual para todas as ações do usuário.
- Código organizado, modular e documentado.
- Compatibilidade com navegadores modernos.
- Cumprimento da LGPD no tratamento de dados sensíveis.
- Retorno rápido nas buscas.

---

## 🧠 Modelagem e Arquitetura

O projeto adota a arquitetura **MVC (Model-View-Controller)**.  
Diagramas utilizados no planejamento:

### Diagrama de Classes

![46fe3f52-67a2-4384-bd14-ad08aba8fdf9](https://github.com/user-attachments/assets/39827ca3-062c-4c86-b5f1-39336c6fe457)

### Diagrama de Casos de Uso

![40f17172-d0e5-4db3-88c4-c9153ab2a95f](https://github.com/user-attachments/assets/5eeab8d2-7a5a-45b2-9035-3548f2930527)

### Modelo Conceitual (Entidades e Atributos)

![015badd8-64b8-4f96-b40c-bf12aedf1ca8](https://github.com/user-attachments/assets/7f910c15-7b5b-4836-a502-e3a4b680a231)

### Modelo Lógico (Tabelas do Banco de Dados)

![ca06c0bd-08db-494f-a9c0-b6cd7f171238](https://github.com/user-attachments/assets/6eabd83c-207b-4a1d-b6aa-86a72aaaf455)

---

## 🖼️ Protótipos de Tela

- Página inicial
- Página de busca de vacinas
- Página de sobre
- Página de Login

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/ianfelps/vacina_certa.git
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente em um arquivo `.env`:

   ```env
   SECRET_KEY=sua_chave_secreta
   GOOGLE_MAPS_API_KEY=sua_api_key
   ```

4. Execute a aplicação:

   ```bash
   python app.py
   ```

5. Acesse em [http://localhost:5000](http://localhost:5000)

---

## 👨‍💻 Contribuidores

- Lucas Homero ([lucas](https://github.com/lucashomero))
- Ian Felipe ([ian](https://github.com/ianfelps))

---

## 📄 Licença

Este projeto é de uso acadêmico e livre para fins educacionais.

---

## 💡 Observações

- O sistema foi desenvolvido para fins didáticos e pode ser expandido para uso real em campanhas de vacinação.
- Sugestões, melhorias e contribuições são bem-vindas!

---

## 🚀 Próximos Passos

1. **Implementação** com base no modelo definido (Flask + SQLite);
2. **Testes manuais** com diferentes cenários e simulações de uso;
3. **Expansões futuras**:
   - 📱 Aplicativo mobile com geolocalização, notificações e experiência otimizada.

---

**Vacina Certa — Informação e tecnologia a serviço da saúde
