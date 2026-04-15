from langchain_community.document_loaders import PyPDFLoader
import os


def load_documents():
    files = [
        "./data/pdfs/auditoria.pdf",
        "./data/pdfs/codigo_etica.pdf",
        "./data/pdfs/politicas.pdf"
    ]

    docs = []

    for file in files:
        if not os.path.exists(file):
            print(f"⚠️ Arquivo não encontrado: {file}")
            continue

        try:
            print(f"📄 Carregando arquivo: {file}")
            loader = PyPDFLoader(file)
            docs.extend(loader.load())
        except Exception as e:
            print(f"❌ Erro ao carregar {file}: {e}")

    print(f"\n✅ Total de documentos carregados: {len(docs)}")

    return docs