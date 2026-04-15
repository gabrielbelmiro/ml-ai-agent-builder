# main.py

from config.env import setup_env
setup_env()

from crewai import Crew, Task
from agents.atendimento import create_atendimento_agent
from agents.pesquisa import create_pesquisa_agent
from agents.resposta import create_resposta_agent

# V1 - FAQ
from tools.faq_tool import buscar_faq

# V2 - RAG
from rag.retriever import get_retriever


# CONFIGURAÇÃO DE MODO
MODO = "rag"
MODO = MODO.strip().lower()


# AGENTES
atendente = create_atendimento_agent()
pesquisador = create_pesquisa_agent()
responder = create_resposta_agent()


# INPUT
pergunta = input("Pergunta do usuário: ")


# CONTEXTO (V1 vs V2)
if MODO == "faq":
    contexto = buscar_faq(pergunta)

elif MODO == "rag":
    retriever = get_retriever()
    docs = retriever.invoke(pergunta)

    if not docs:
        contexto = "Não encontrei essa informação na base de conhecimento. Poderia fornecer mais detalhes ou reformular a pergunta?"
    else:
        contexto = "\n".join(doc.page_content for doc in docs)

else:
    contexto = "Modo inválido. Use 'faq' ou 'rag'."


# TASKS

task1 = Task(
    description=f"Entenda a intenção da pergunta: {pergunta}",
    expected_output="Análise da intenção do usuário.",
    agent=atendente
)

task2 = Task(
    description=f"""
Use apenas o contexto abaixo para responder:

{contexto}
""",
    expected_output="Resposta baseada exclusivamente no contexto.",
    agent=pesquisador
)

task3 = Task(
    description=f"""
Responda a pergunta com base apenas no contexto.

Pergunta: {pergunta}

Contexto:
{contexto}

Regras:
- Não inventar
- Não usar conhecimento externo
- Se não encontrar, diga que não encontrou
""",
    expected_output="Resposta clara e fiel ao contexto.",
    agent=responder
)


# CREW

crew = Crew(
    agents=[atendente, pesquisador, responder],
    tasks=[task1, task2, task3],
    verbose=True
)

resultado = crew.kickoff()

print("\nResposta final:\n", resultado)
