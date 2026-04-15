from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def get_retriever():
    embeddings = OpenAIEmbeddings()

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 2})