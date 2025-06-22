# Projeto (Vacina Certa)

O Vacina Certa é uma plataforma web desenvolvida como resposta à dificuldade enfrentada pela população do Distrito Federal em obter informações claras, centralizadas e atualizadas sobre a disponibilidade de vacinas e campanhas de vacinação nos postos de saúde.
O objetivo principal é simplificar o acesso à informação, reduzir deslocamentos desnecessários e combater a desinformação, garantindo que os cidadãos possam encontrar os imunizantes que precisam de forma rápida e segura.

---

## 📌 Objetivo

O **Vacina Certa** surgiu como resposta à dificuldade enfrentada por cidadãos para encontrar informações confiáveis sobre:

- Disponibilidade de vacinas;
- Localização dos postos de saúde;
- Campanhas de vacinação ativas;
- Esclarecimento de dúvidas frequentes.

A proposta é **centralizar e simplificar o acesso à informação**, promovendo confiança, agilidade e prevenção.

---

## 💡 Funcionalidades

- Exibição de campanhas em destaque na página inicial;
- Busca por tipo de vacina e por região administrativa (RA) do DF;
- Mapa interativo com os postos de saúde que oferecem cada vacina;
- Níveis de estoque representados visualmente (cheio, moderado, vazio);
- Página institucional com perguntas frequentes (FAQ) e “Quem Somos”.

---

## 🛠️ Tecnologias Utilizadas

| Camada        | Ferramentas                          |
|---------------|--------------------------------------|
| Back-end      | Python, Flask                        |
| Front-end     | HTML, CSS, JavaScript, Bootstrap     |
| Banco de Dados| SQLite                               |
| Mapa          | Folium                               |

---

## 📋 Requisitos

### ✨ Funcionalidades Principais

- Busca de Vacinas: Sistema de consulta para verificar a disponibilidade de vacinas específicas.
- Mapa Interativo: Ferramenta de geolocalização para visualizar os postos de saúde e as vacinas disponíveis em cada um.
- Campanhas em Destaque: Seção dedicada à divulgação clara de campanhas de vacinação em andamento no DF.
- Área Informativa: Espaço com perguntas e respostas frequentes para esclarecer dúvidas da população sobre os imunizantes.
  
### 🔒 Não Funcionais

- Interface simples e acessível;
- Retorno rápido nas buscas;
- Segurança com autenticação na área administrativa;
- Banco de dados leve (SQLite);
- Adequação à LGPD mesmo sem coletar dados sensíveis.

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

### Página inicial

### Página de busca de vacinas

### Página de perguntas frequentes (FAQ)

---

## 🚀 Próximos Passos

1. **Implementação** com base no modelo definido (Flask + SQLite);
2. **Testes manuais** com diferentes cenários e simulações de uso;
3. **Expansões futuras**:
   - 🔐 Painel administrativo com login e edição de dados;
   - 📱 Aplicativo mobile com geolocalização, notificações e experiência otimizada.

---

## ⚙️ Como Executar o Projeto

---
