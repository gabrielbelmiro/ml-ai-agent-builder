def buscar_faq(pergunta: str) -> str:
    with open("data/faq.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    return f"""
Você deve responder usando APENAS a base abaixo.

BASE DE CONHECIMENTO:
{conteudo}

PERGUNTA:
{pergunta}

Se a resposta não estiver na base, diga que a informação não foi encontrada na base de conhecimento.
"""