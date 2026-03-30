import streamlit as st
import requests

def load_syllabus():
    with open("syllabus.txt", "r") as f:
        return f.read()

def create_prompt(question, syllabus):
    prompt = f"""
You are a syllabus FAQ assistant.
Answer only from the syllabus topics below.
If question is outside syllabus, say "Not in syllabus".

Syllabus:
{syllabus}

Question:
{question}

Answer:
"""
    return prompt

def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    data=response.json()
    return data.get("response",str(data))

st.title("Smart Syllabus FAQ Chatbot")

syllabus = load_syllabus()
question = st.text_input("Ask a syllabus question:")

if st.button("Ask"):
    prompt = create_prompt(question, syllabus)
    answer = ask_llm(prompt)
    st.write("Answer:", answer)