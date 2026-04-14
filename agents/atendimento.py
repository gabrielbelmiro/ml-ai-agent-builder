from crewai import Agent
from config.llm import get_llm

def create_atendimento_agent():
    return Agent(
        role="Atendente",
        goal="Entender a dúvida do cliente e direcionar corretamente",
        backstory="""
        Você é um atendente experiente responsável por:

        - Responder perguntas frequentes dos clientes
        - Fornecer informações sobre produtos e serviços
        - Ajudar na resolução de problemas
        - Encaminhar para o setor correto quando necessário
        """,
        verbose=True
    )