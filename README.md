##TwinMind AI – Intelligent Digital Twin Assistant

## Overview

TwinMind AI is an AI-powered Digital Twin Assistant that enables users to interact with technical documents through natural language. By leveraging Retrieval-Augmented Generation (RAG), the application retrieves relevant information from uploaded documents and generates accurate, context-aware responses using a Large Language Model.

The project demonstrates how modern AI technologies such as vector databases, embeddings, and LLMs can be integrated to build an intelligent document assistant.

## Features

*  Upload and process PDF documents
*  Interactive chatbot interface
*  Retrieval-Augmented Generation (RAG)
*  Fast inference using Groq LLM
*  Semantic search using FAISS vector database
*  Context-aware responses based on uploaded documents
*  Simple and user-friendly Streamlit interface

## Technology Stack

**Frontend**

* Streamlit

**Backend**

* Python

**AI & Machine Learning**

* Groq LLM (Llama 3.1)
* Sentence Transformers
* FAISS Vector Database

**Libraries**

* PyPDF2
* Requests
* NumPy
* FAISS-CPU
* Sentence Transformers

## System Workflow

1. User uploads one or more PDF documents.
2. The documents are extracted and divided into text chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored in a FAISS vector database.
5. When the user asks a question, the query is converted into an embedding.
6. FAISS retrieves the most relevant document chunks.
7. The retrieved context is combined with the user's question.
8. Groq Llama 3.1 generates a context-aware response.
9. The answer is displayed through the Streamlit interface.

## Applications

* Intelligent document assistant
* Research paper analysis
* Technical documentation chatbot
* Educational learning assistant
* Enterprise knowledge management
* Digital Twin support systems

## Future Improvements

* Multi-document knowledge base
* Voice-based interaction
* Image and diagram understanding
* Cloud deployment
* User authentication
* Conversation history persistence
* API integration with external knowledge sources

## Installation

```bash
git clone <repository-url>
cd TwinMind-AI

pip install -r requirements.txt

streamlit run app.py
```

## Project Structure

```
TwinMind-AI/
│── app.py
│── requirements.txt
│── README.md
│── data/
│── vector_store/
│── utils/
└── assets/
```

## Author

**Preran C V N**

Bachelor of Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, RAG Systems, and Intelligent Automation.
