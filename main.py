# main.py

from config.env import setup_env
setup_env()

from crewai import Crew, Task
from agents.atendimento import create_atendimento_agent
from agents.pesquisa import create_pesquisa_agent
from agents.resposta import create_resposta_agent

# V1 - FAQ
from tools.faq_tool import buscar_faq

# V2/V3 - RAG
from rag.retriever import get_retriever
from rag.guardrails import validate_context, FALLBACK_MESSAGE
from rag.formatter import extract_sources, confidence_score


# CONFIGURAÇÃO DE MODO
MODO = "rag"
MODO = MODO.strip().lower()


# AGENTES
atendente = create_atendimento_agent()
pesquisador = create_pesquisa_agent()
responder = create_resposta_agent()


# INPUT
pergunta = input("Pergunta do usuário: ")


# CONTEXTO (V1 vs V2/V3)
docs = []
fontes = ""
score = "baixa"

if MODO == "faq":
    contexto = buscar_faq(pergunta)

elif MODO == "rag":
    retriever = get_retriever()
    docs = retriever.invoke(pergunta)

    # Reduzir ruido do RAG: se não houver documentos, contexto vazio. Se houver, extrair apenas o conteúdo relevante.
    docs = docs[:1]  # Limitar a 1 documento para reduzir ruido em leis e normas, mas pode ser ajustado para 2 ou 3 dependendo do caso.

    if not docs:
        contexto = ""
    else:
        contexto = "\n".join(doc.page_content for doc in docs)

    # Guardrail: valida se existe contexto aproveitável
    if not validate_context(contexto):
        contexto = ""
    else:
        fontes = extract_sources(docs)
        score = confidence_score(docs)

else:
    contexto = ""


# TASKS

task1 = Task(
    description=f"Entenda a intenção da pergunta: {pergunta}",
    expected_output="Análise da intenção do usuário.",
    agent=atendente
)

task2 = Task(
    description=f"""
Use apenas o contexto abaixo para responder à pergunta do usuário.

Pergunta:
{pergunta}

Contexto:
{contexto if contexto else FALLBACK_MESSAGE}

Regras:
- Responda apenas com base no contexto fornecido.
- Se a informação não estiver no contexto, responda exatamente:
"{FALLBACK_MESSAGE}"
- Não utilize conhecimento externo.
""",
    expected_output="Resposta baseada exclusivamente no contexto ou fallback.",
    agent=pesquisador
)

task3 = Task(
    description=f"""
Responda à pergunta com base apenas no contexto abaixo.

Pergunta:
{pergunta}

Contexto:
{contexto if contexto else FALLBACK_MESSAGE}

Regras:
- Use SOMENTE frases presentes no contexto.
- NÃO reescreva, NÃO interprete e NÃO complemente.
- NÃO adicione explicações.
- Copie apenas o trecho relevante do contexto.
- Se não encontrar exatamente no contexto, responda:
"{FALLBACK_MESSAGE}"
""",
    expected_output="Resposta extraída diretamente do contexto, sem modificações.",
    agent=responder
)


# CREW

crew = Crew(
    agents=[atendente, pesquisador, responder],
    tasks=[task1, task2, task3],
    verbose=True
)

resultado = crew.kickoff()


# SAÍDA FINAL CONTROLADA
if not contexto:
    print("\nResposta final:\n", FALLBACK_MESSAGE)
else:
    print("\nResposta final:\n", resultado)
    print(f"\nFonte: {fontes}")
    print(f"Confiança: {score}")