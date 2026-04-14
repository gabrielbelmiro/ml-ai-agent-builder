# main.py
import os
from config.settings import settings

# CyberSecurity: Definir ambiente ANTES de importar os agents / crewai
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

from crewai import Crew, Task
from agents.atendimento import create_atendimento_agent
from agents.pesquisa import create_pesquisa_agent
from agents.resposta import create_resposta_agent
from tools.faq_tool import buscar_faq

atendente = create_atendimento_agent()
pesquisador = create_pesquisa_agent()
responder = create_resposta_agent()

pergunta = input("Pergunta do usuário: ")

task1 = Task(
    description=f"Entenda a intenção da pergunta: {pergunta}",
    expected_output="Uma análise breve da intenção do usuário e do tipo de informação necessária.",
    agent=atendente
)

task2 = Task(
    description=buscar_faq(pergunta),
    expected_output="Um resumo objetivo baseado exclusivamente na base de conhecimento fornecida.",
    agent=pesquisador
)

task3 = Task(
    description=f"""
Com base apenas nas informações coletadas na etapa anterior, responda claramente à pergunta do usuário.

Pergunta: {pergunta}
""",
    expected_output="Uma resposta final clara, objetiva e fiel à base consultada.",
    agent=responder
)

crew = Crew(
    agents=[atendente, pesquisador, responder],
    tasks=[task1, task2, task3],
    verbose=True
)

resultado = crew.kickoff()
print("\nResposta final:\n", resultado)
