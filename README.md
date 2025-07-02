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

![image](https://github.com/user-attachments/assets/33edccc0-89d6-44f5-80f9-a21366338e9a)

### Diagrama de Casos de Uso

![image](https://github.com/user-attachments/assets/2276acc2-bcbc-4ed9-96ec-5ba726dabc82)

### Modelo Conceitual (Entidades e Atributos)

![image](https://github.com/user-attachments/assets/33998f2c-68fa-4b60-bf13-88ad2e43b278)

### Modelo Lógico (Tabelas do Banco de Dados)

![image](https://github.com/user-attachments/assets/04a7e071-3f7a-460d-b8de-cecef12d8e24)

---

## 🖼️ Telas do Sistema

- Página inicial
![PáginaInicial](https://github.com/user-attachments/assets/454656ec-72dc-491c-8e72-cbeac52b3794)

- Página de busca de vacinas
![Página de Busca](https://github.com/user-attachments/assets/ffac3a91-e315-42e8-a686-476f99b46447)

- Página de sobre
![Página de Sobre](https://github.com/user-attachments/assets/b14cd5e0-061c-48c8-89bb-5a932bf31ed7)

- Páginas de Administrador
  - ![Login](https://github.com/user-attachments/assets/c9df22b0-1ccf-4863-8eb8-6adbe20c8e9f)
  - ![PosLogin](https://github.com/user-attachments/assets/40747ba5-8647-44a2-8443-25c3937fe5a2)
  - ![Edicao](https://github.com/user-attachments/assets/3edd451b-2a22-4363-9425-c2454eaf9035)
  - ![Vacinas](https://github.com/user-attachments/assets/97e5966a-0b83-48d2-834b-dc7d39a50884)
  - ![EdicaoVacinas](https://github.com/user-attachments/assets/ea63b05a-45ce-4957-b18a-e649dd6c8388)
  - ![SaldoVacinas](https://github.com/user-attachments/assets/6936dd81-ef1b-4dd0-9390-6da862057da6)
  - ![EdicaoVacinas](https://github.com/user-attachments/assets/226beb60-c452-4cc6-82e6-53e6c96557f1)

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/1thallo/Vacina_Certa.git
   ```

2. Configure as variáveis de ambiente em um arquivo `.env`:

   ```env
   SECRET_KEY=sua_chave_secreta
   GOOGLE_MAPS_API_KEY=sua_api_key
   ```

3. Crie um arquivo `admin_users.py`, onde ficará os dados de acesso para página de administrador:

    ```plaintext
    ADMIN = {
        "nomelogin" : "senha"
    }
    ```

4. Execute a aplicação:

   ```bash
   python app.py
   ```

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
   - 📱 Aplicativo mobile com geolocalização, notificações e experiência mobile otimizada.

---

** Vacina Certa — Informação e tecnologia a serviço da saúde
