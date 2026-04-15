import os

def extract_sources(docs):
    fontes = set()

    for doc in docs:
        nome = os.path.basename(doc.metadata.get("source", "desconhecido"))
        fontes.add(nome)

    return ", ".join(sorted(fontes))


def confidence_score(docs):
    fontes_unicas = set()

    for doc in docs:
        nome = os.path.basename(doc.metadata.get("source", "desconhecido"))
        fontes_unicas.add(nome)

    total_fontes = len(fontes_unicas)

    if total_fontes == 0:
        return "baixa"
    elif total_fontes == 1:
        return "alta"
    elif total_fontes == 2:
        return "média"
    else:
        return "baixa"