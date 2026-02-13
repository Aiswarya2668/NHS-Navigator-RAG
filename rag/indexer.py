import faiss
import numpy as np
import ollama

def create_faiss_index(embeddings):
    """Create a FAISS index from embeddings."""
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def retrieve(query, index, chunks, k=2):
    """Retrieve top-k relevant chunks from FAISS index."""
    query_embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=query
    )["embedding"]

    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]