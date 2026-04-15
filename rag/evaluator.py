# Avaliação da resposta do agente RAG pode ser feita de forma simples, considerando a presença de fontes e a quantidade de informações retornadas. 
# Aqui está uma função que avalia a resposta com base nesses critérios:
def evaluate_response(contexto: str, resposta: str) -> str:
    if "Não encontrei" in resposta:
        return "baixa"

    if len(contexto) < 100:
        return "média"

    return "alta"