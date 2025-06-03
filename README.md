# Chat with Multiple PDFs

A Streamlit app that allows you to upload multiple PDF documents, process them, and interactively chat with the content using a conversational AI. The app splits PDFs into chunks, creates vector embeddings, and performs retrieval-augmented conversation with the documents.
This project is a Streamlit-based web application that allows users to upload multiple PDF documents and interactively chat with their combined content using a powerful language model. It extracts text from PDFs, splits it into manageable chunks, and creates a semantic vector store for efficient retrieval. Users can ask questions related to their documents and get meaningful answers based on the uploaded content.

The app integrates local LLMs (like Gemma3 or HuggingFace models) for conversational AI and supports memory to maintain chat context. This makes it an excellent tool for exploring large collections of PDFs—perfect for research, study, or knowledge management.

---

## Features

- Upload multiple PDF files at once
- Extract and split PDF text into manageable chunks
- Create semantic vector embeddings for fast retrieval
- Use a local or HuggingFace language model for conversational Q&A
- Maintain conversation history with memory support
- Simple and clean Streamlit user interface

---

## Tech Stack

- Python 3.8+
- [Streamlit](https://streamlit.io/) for the web UI
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction
- [LangChain](https://python.langchain.com/) for LLM chaining and retrieval
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index) (optional) for embeddings and chat models
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management


