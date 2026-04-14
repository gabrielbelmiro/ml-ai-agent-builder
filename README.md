# 🤖 AI Agent Builder - Customer Support com CrewAI
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Projeto demonstrando uma arquitetura de múltiplos agentes utilizando CrewAI para simular um cenário real de atendimento automatizado.

---

## 🚀 Funcionalidades

- 🤖 Atendimento automatizado com AI Agents
- 🧠 Interpretação de intenção do usuário
- 🔎 Pesquisa em base de conhecimento (FAQ)
- 💬 Geração de resposta baseada em contexto
- 🔗 Orquestração de múltiplos agentes
- 🏗️ Arquitetura modular e escalável

---

## 🧠 Arquitetura do Sistema

O sistema é composto por três agentes especializados:

- **Atendente**
  - Interpreta a intenção do usuário
  - Define o contexto da solicitação

- **Pesquisador**
  - Consulta a base de conhecimento (FAQ)
  - Recupera informações relevantes

- **Respondedor**
  - Gera a resposta final
  - Garante clareza e objetividade

---

## 📂 Estrutura do Projeto
```bash
ml-ai-agent-builder/
├── agents/
├── config/
├── tools/
├── data/
│   └── faq.txt
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- Python
- CrewAI (Multi-Agent Orchestration)
- LLM (OpenAI)
- Keyring (armazenamento seguro de credenciais)

---

## 🔐 Segurança

Este projeto utiliza armazenamento seguro de credenciais via **Windows Credential Manager (keyring)**, evitando exposição de chaves sensíveis no código.

---

## ⚙️ Como Configurar

```
# Clonar o projeto
git clone https://github.com/SEU-USUARIO/ml-ai-agent-builder.git 
cd ml-ai-agent-builder

# criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# instalar keyring (caso necessário)
pip install keyring

## 🔐 Configurar API Key
import keyring
keyring.set_password("openai", "api_key", "SUA_OPENAI_API_KEY")
exit()

## ▶️ Executar
python main.py

## 💬 Exemplo de pergunta
Pergunta do usuário: Política de Compras e Suprimentos
```
--- 
## 👨‍💻 Autor

Gabriel Belmiro 🔗 https://www.linkedin.com/in/gabriel-belmiro/

Desenvolvedor em constante evolução, com foco em fundamentos sólidos, organização de código e crescimento progressivo em arquitetura e boas práticas.