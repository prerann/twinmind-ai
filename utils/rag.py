import os
import faiss
import numpy as np
from models.embeddings import get_embedding

documents = []
index = None

def load_documents(folder_path="data"):
    global documents
    documents = []

    if not os.path.exists(folder_path):
        return

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append(f.read())

def create_vector_store():
    global index

    if not documents:
        return

    embeddings = [get_embedding(doc) for doc in documents]
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

def add_document(text):
    global documents, index

    documents.append(text)

    emb = np.array([get_embedding(text)]).astype("float32")

    if index is None:
        index = faiss.IndexFlatL2(emb.shape[1])

    index.add(emb)

def retrieve_context(query, top_k=1):
    global index

    if index is None:
        return ""

    query_embedding = np.array([get_embedding(query)]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    return documents[indices[0][0]]