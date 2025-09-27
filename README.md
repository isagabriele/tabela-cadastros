# Tabela Dinâmica com Google Sheets - Alpha Fitness

*Projeto que exibe dados de uma planilha do Google Sheets em uma interface web responsiva com atualizações automáticas, estilizado com a identidade visual da Rede Alpha Fitness.*

---

### ✨ Demonstração

![Demonstração da Aplicação](https://github.com/user-attachments/assets/725cbf8f-0781-4d96-bea8-8bf6634c463d)

---

### 📖 Descrição

Este projeto foi desenvolvido para consumir dados de uma Planilha Google e exibi-los de forma clara e dinâmica em uma página web. O backend, construído em Python com o microframework Flask, é responsável por ler os dados, realizar validações (CPF, Telefone) e formatações, e servi-los através de uma API. O frontend, desenvolvido com HTML, CSS e JavaScript puro, consome essa API e constrói a tabela de forma responsiva, atualizando-a periodicamente sem a necessidade de recarregar a página.

---

### 🚀 Funcionalidades

-   **Leitura de Dados em Tempo Real:** Conexão direta com a API do Google Sheets.
-   **Atualização Automática:** O frontend verifica por novos dados a cada 1 minuto.
-   **Backend Robusto:** API RESTful desenvolvida com Flask para servir os dados.
-   **Tratamento e Validação de Dados:**
    -   Validação completa de CPF (cálculo de dígitos verificadores).
    -   Validação de número de telefone no padrão brasileiro (`+55 (XX) 9XXXX-XXXX`).
    -   Formatação de `timestamp` para o padrão `dd/mm/aaaa HH:MM:SS`.
-   **Frontend Dinâmico:** A tabela é construída dinamicamente com JavaScript, adaptando-se a qualquer quantidade de colunas.
-   **Design Responsivo:** O layout se adapta a diferentes tamanhos de tela (desktop, tablet e mobile).

---

### 🛠️ Tecnologias Utilizadas

<div style="display: inline_block"><br>
  <img align="center" alt="HTML5" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
  <img align="center" alt="CSS3" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">
  <img align="center" alt="JavaScript" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Flask" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg">
</div>

-   **Frontend:** HTML5, CSS3, JavaScript
-   **Backend:** Python, Flask, Pandas, gspread
-   **Hospedagem:** Render

---

### ⚙️ Como Executar o Projeto Localmente

**Pré-requisitos:**
-   Python 3.x
-   Git

```bash
# 1. Clone o repositório
git clone https://github.com/isagabriele/tabela-cadastros.git

# 2. Navegue até a pasta do projeto
cd tabela-cadastros

# 3. Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 4. Instale as dependências
pip install -r backend/requirements.txt