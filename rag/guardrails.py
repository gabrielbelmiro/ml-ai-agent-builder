FALLBACK_MESSAGE = "Não encontrei essa informação na base de conhecimento. Poderia fornecer mais detalhes ou reformular a pergunta?"

def validate_context(contexto: str) -> bool:
    return contexto.strip() != "" and "Não encontrei" not in contexto