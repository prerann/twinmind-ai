import streamlit as st
from models.llm import generate_response
from utils.rag import load_documents, create_vector_store, retrieve_context, add_document
from utils.web_search import search_web

st.set_page_config(page_title="TwinMind AI", layout="wide")

st.title("🤖 TwinMind AI - Digital Twin Assistant")

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load RAG once
if "loaded" not in st.session_state:
    load_documents()
    create_vector_store()
    st.session_state.loaded = True

# Upload file
uploaded_file = st.file_uploader("Upload TXT file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    add_document(text)
    st.success("Document added to knowledge base!")

# Response mode
mode = st.radio("Response Mode:", ["Concise", "Detailed"])

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 🔥 Step 1: Get RAG context
    context = retrieve_context(user_input)

    # 🔥 Step 2: SMART decision (FIXED)
    if context and user_input.lower() in context.lower():
        final_context = context
        source = "📄 RAG"
    else:
        final_context = search_web(user_input)
        source = "🌐 Web"

    # 🔥 Step 3: Prompt
    if mode == "Concise":
        prompt = f"Answer briefly using this context:\n{final_context}\n\nQuestion: {user_input}"
    else:
        prompt = f"Answer in detail using this context:\n{final_context}\n\nQuestion: {user_input}"

    messages = [
        {"role": "system", "content": "You are an AI assistant for robotics and digital twin systems."},
        {"role": "user", "content": prompt}
    ]

    # 🔥 Step 4: Generate response
    response = generate_response(messages)

    # Show response
    with st.chat_message("assistant"):
        st.write(f"{response}\n\n({source})")

    st.session_state.messages.append({"role": "assistant", "content": response})