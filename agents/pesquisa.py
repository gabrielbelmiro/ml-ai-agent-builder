from crewai import Agent
from config.llm import get_llm

def create_pesquisa_agent():
    return Agent(
        role="Pesquisador",
        goal="Realizar pesquisas e coletar informações relevantes para a empresa",
        backstory="""
        Você é um especialista em pesquisa e recuperação de informações.
        Seu papel é localizar dados relevantes para apoiar a resposta ao usuário.
        Você trabalha em conjunto com o Atendente e o agente de Resposta.
        """,
        verbose=True
    )