import numpy as np
import ollama

def create_embeddings(chunks):
    """Generate embeddings for each text chunk using Ollama."""
    embeddings = []
    for chunk in chunks:
        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=chunk
        )
        embeddings.append(response["embedding"])
    return np.array(embeddings).astype("float32")