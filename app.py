import streamlit as st
from rag.loader import load_pdfs, chunk_text
from rag.embeddings import create_embeddings
from rag.indexer import create_faiss_index, retrieve
from rag.generator import generate_answer


# -----------------------------
# Initialize RAG system
# -----------------------------
@st.cache_data
def initialize_rag(knowledge_folder="knowledge"):
    documents = load_pdfs(knowledge_folder)
    all_chunks = []
    for doc in documents:
        all_chunks.extend(chunk_text(doc))
    embeddings = create_embeddings(all_chunks)
    index = create_faiss_index(embeddings)
    return all_chunks, index


all_chunks, index = initialize_rag()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title(" 🏥👾 RAG Assistant for NHS 🩺")
st.write("Query your NHS and business documents. Receive concise, easy-to-read answers in bullet points.")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Input box
query = st.text_input("Your Question:")

if query:
    with st.spinner("Retrieving answer..."):
        # Retrieve relevant chunks and generate answer
        retrieved_chunks = retrieve(query, index, all_chunks, k=3)
        answer = generate_answer(query, retrieved_chunks)

        # Add to history
        st.session_state['history'].append((query, answer))

# -----------------------------
# Display Q&A history
# -----------------------------
if st.session_state['history']:
    st.subheader("💬 Q&A History")
    for i, (q, a) in enumerate(st.session_state['history'][::-1]):  # show newest first
        st.markdown(f"**Q{i + 1}: {q}**")
        st.markdown(f"**A{i + 1}:** {a}")
        st.markdown("---")

# Optional: show retrieved chunks for last query
if query:
    with st.expander("Show Retrieved Chunks"):
        for i, chunk in enumerate(retrieved_chunks):
            st.write(f"Chunk {i + 1}: {chunk[:300]}...")