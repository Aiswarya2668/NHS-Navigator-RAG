import ollama

def generate_answer(query, context_chunks):
    """
    Generate a concise, human-readable answer based on retrieved context.

    - Summarizes in 2-5 bullet points
    - Paraphrases instead of copying
    - Uses simple, clear business language
    """
    context = "\n\n".join(context_chunks)
    prompt = f"""
You are a professional business assistant.
Answer the question using ONLY the provided context.
- Summarize the answer concisely in 2-5 bullet points.
- Paraphrase information; avoid copying exact sentences.
- Use simple and clear language suitable for a business executive.

Context:
{context}

Question:
{query}

Answer:
"""

    # Optional: add system role for better summarization
    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "system", "content": "You are a concise business strategy assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]