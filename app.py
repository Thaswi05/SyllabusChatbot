import streamlit as st
import requests
import os

def load_syllabus(year):
    file_path = f"syllabus/year{year}.txt"
    with open(file_path, "r") as file:
        return file.read()

def create_prompt(question, syllabus):
    return f"""
You are a university syllabus chatbot.
Answer the question using only the syllabus information below.
If the user asks for a definition, explain the topic.
If the user asks for subjects or topics, list them clearly.

Syllabus Information:
{syllabus}

Question:
{question}

Answer:
"""
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

st.title("University Syllabus Chatbot")

year = st.selectbox("Select Year", [1, 2, 3, 4])
question = st.text_input("Ask a syllabus question:")

if st.button("Ask"):
    syllabus = load_syllabus(year)
    prompt = create_prompt(question, syllabus)
    answer = ask_llm(prompt)
    st.write("Answer:", answer)