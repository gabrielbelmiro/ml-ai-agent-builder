import os
from config.settings import settings

# 🔐 Define API KEY (igual main.py)
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
from rag.retriever import get_retriever

def test_rag():
    retriever = get_retriever()

    pergunta = input("Pergunta para teste: ")

    docs = retriever.invoke(pergunta)

    print("\n📄 DOCUMENTOS RECUPERADOS:\n")

    for i, doc in enumerate(docs):
        print(f"\n--- Documento {i+1} ---")
        print(f"Fonte: {doc.metadata.get('source')}")
        print(doc.page_content)

    if not docs:
        print("\n⚠️ Nenhum documento encontrado")
    else:
        contexto = "\n".join(doc.page_content for doc in docs)

        print("\n🧠 CONTEXTO FINAL:\n")
        print(contexto)


if __name__ == "__main__":
    test_rag()