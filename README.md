


# 🤖🏥 NHS-Navigator-RAG

Interactive RAG (Retrieval-Augmented Generation) bot for querying **NHS and business-related PDFs**. Ask questions and get **concise bullet-point answers** with relevant context.

---
## 🛠️ Technologies Used

This project leverages the following technologies:

- **Python** – Core programming language for all scripts
- **RAG (Retrieval-Augmented Generation)** – Combines retrieval of relevant documents with AI-based answer generation  
- **Streamlit** – Interactive front-end web interface  
- **PyPDF2** – Extract text from PDF documents  
- **Ollama** – Generate embeddings and answers using AI models (`nomic-embed-text` & `phi3`)  
- **FAISS** – Fast similarity search for retrieving relevant text chunks  
- **NumPy** – Numerical operations on embeddings  
- **Virtual Environment** – Isolated Python environment for dependencies  
- **Git & GitHub** – Version control and project hosting  

---

## ✨ Features

- Torch-free, local RAG system (no GPU needed)  
- Load multiple PDFs from the `knowledge/` folder  
- Generate **concise, paraphrased bullet-point answers**  
- Supports **NHS & business documents** in the same knowledge base  
- **Interactive Streamlit front-end**  
- **Q&A history** to track previous questions and answers  
- Optional: view **retrieved chunks** for transparency  

---

## 📂 Project Structure


<img width="1065" height="591" alt="image" src="https://github.com/user-attachments/assets/5b04872f-8888-42cc-a61d-30b875fe741c" />



---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/Aiswarya2668/NHS-Navigator-RAG.git
```


2. Create a virtual environment :
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
.venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Add your PDFs to the knowledge/ folder.

---

## 🚀 Running the Bot

Start the Streamlit interface:

```bash
streamlit run app.py
```

Type your questions in the input box.

Get answers in bullet points.

Expand Q&A history to view previous queries and answers.

Optionally, expand Retrieved Chunks to see source text from PDFs.

---

## Example Questions

### NHS Questions:

- Summarize the NHS Long Term Plan.

- What are the key priorities for NHS digital transformation?

- What rights do patients have under the NHS Constitution?

### Business & Analytics Questions:

- Summarize the digital transformation plan for the business unit.

- What are the key points in our marketing strategy for 2025?

- How is data used to improve decision-making?

### Data Analyst Insights:

- How many data analysts work in the NHS?

- What are the future challenges for NHS data analytics by 2030?

- Summarize key analytics achievements from the NHS Annual Impact Report.

---

## 🛠️ How It Works

1. Load PDFs → Convert to text and split into chunks
2. Create embeddings → Ollama embeddings for each chunk
3. FAISS index → Fast retrieval of relevant chunks
4. Retrieve top-k chunks → Based on user query
5. Generate answer → Ollama chat produces concise bullet-point answers
6. Display in Streamlit → Interactive web interface with history

