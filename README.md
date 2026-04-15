# 🤖 AI Agent Builder - Multi-Agent Customer Support com RAG (CrewAI)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Projeto demonstrando uma arquitetura de múltiplos agentes utilizando CrewAI para simular um cenário real de atendimento automatizado.

---

## 🚀 Funcionalidades

- 📄 RAG com documentos PDF (busca semântica)
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
├── rag/
├── tools/
├── data/
│   ├── faq.txt
│   └── pdfs/
├── debug/
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
```
---


## ▶️ Executar
```
## Rodar 
python main.py

## 💬 Exemplo de atendimento

# Entrada (INPUT)
Pergunta do usuário: Política de Compras e Suprimentos

# Saída (Output)
"A Política de Compras e Suprimentos define os critérios para a seleção de fornecedores, estabelecendo
que é necessário obter, no mínimo, três orçamentos. Além disso, a política inclui a realização de uma 
análise de risco (due diligence) para garantir a segurança e a conformidade das aquisições realizadas.
Essas diretrizes visam assegurar transparência, eficiência e responsabilidade nas compras da organização."
```
---

## 🧠 Destaque do Exemplo

Este exemplo demonstra:

- ✔️ Relação clara entre entrada (input) e saída (output)  
- ✔️ Execução real do sistema em ambiente controlado  
- ✔️ Uso de grounding com base de conhecimento local  
- ✔️ Geração de respostas contextualizadas e confiáveis  

👉 Exemplo baseado em execução real utilizando a base de conhecimento interna do projeto.

---

## 🎯 Objetivo do Projeto

A evolução do projeto visa sair de uma base estática (FAQ em texto) para uma arquitetura escalável baseada em RAG, simulando cenários reais de uso corporativo com grandes volumes de dados.

## 🚀 Evolução do Projeto (Roadmap)

### ✅ Versão 1 - FAQ (TXT)
- Base de conhecimento em arquivo `.txt`
- Grounding simples com contexto estático
- Arquitetura multi-agente com CrewAI
- Separação de responsabilidades (Atendente, Pesquisador, Respondedor)
- Foco em estrutura, orquestração e funcionamento do fluxo

---

### ✅ Versão 2 - RAG com PDFs
- Ingestão de documentos PDF (ex: políticas, auditorias, normas)
- Processamento e chunking de documentos
- Vetorização com embeddings
- Busca semântica (Retrieval-Augmented Generation)
- Respostas baseadas em contexto dinâmico
- Escalabilidade para bases maiores e cenários corporativos

---

### 🔜 Versão 3 - Guardrails e Redução de Alucinação
- Respostas restritas ao contexto recuperado
- Fallback para perguntas fora da base ("informação não encontrada")
- Engenharia de prompts com regras mais rígidas
- Citação da fonte utilizada na resposta
- Score de confiança da resposta (alta/média/baixa)
- Avaliação automática de qualidade das respostas
- Logs e observabilidade (erros, falhas e inconsistências)

🚧 Projeto em evolução contínua: V3 (Guardrails, fonte e avaliação de respostas) em desenvolvimento.

---


## 👨‍💻 Autor

Gabriel Belmiro 🔗 https://www.linkedin.com/in/gabriel-belmiro/

Desenvolvedor em constante evolução, com foco em fundamentos sólidos, organização de código e crescimento progressivo em arquitetura e boas práticas.