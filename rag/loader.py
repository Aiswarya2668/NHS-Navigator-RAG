import os
from pathlib import Path
from PyPDF2 import PdfReader

def load_pdfs(folder_path):
    """Load all PDFs in a folder and extract text."""
    documents = []
    folder = Path(folder_path)
    for pdf_file in folder.glob("*.pdf"):
        text = ""
        try:
            reader = PdfReader(str(pdf_file))
            for page in reader.pages:
                text += page.extract_text() or ""
            documents.append(text)
        except Exception as e:
            print(f"⚠️ Could not read {pdf_file.name}: {e}")
    return documents

def chunk_text(text, chunk_size=500):
    """Split text into fixed-size chunks."""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks