from crewai import Agent
from config.llm import get_llm 

def create_resposta_agent():
    return Agent(
        role="Resposta",
        goal="Gerar respostas claras e precisas para sanar as dúvidas dos clientes",
        backstory="""
            Especialista em fornecer respostas rápidas e concisas com base nas informações disponíveis
            Capaz de entender a dúvida do cliente e fornecer uma resposta adequada clara e objetiva
            Utiliza informações coletadas pelo Pesquisador para responder às perguntas dos clientes
       """,
        verbose=True
    )