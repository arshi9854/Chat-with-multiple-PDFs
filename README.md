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


##How It Works


![PDF-LangChain](https://github.com/user-attachments/assets/071912b1-fa04-4a22-8cf8-286092df1ca0)

The application follows these steps to provide responses to your questions
-PDF Loading: The app reads multiple PDF documents and extracts their text content
-Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.
-Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.
-Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
-Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

##Dependencies and Installation
To install the MultiPDF Chat App, please follow these steps:
-Clone the repository to your local machine.
-Install the required dependencies by running the following command:
  pip install -r requirements.txt
-Obtain an API key from OpenAI and add it to the .env file in the project directory or use the huggingface model directly by providing the model's URL.
-OPENAI_API_KEY=your_secrit_api_key

##Usage
To use the MultiPDF Chat App, follow these steps:
-Ensure that you have installed the required dependencies and added the OpenAI API key to the .env file.
-Run the main.py file using the Streamlit CLI. Execute the following command:streamlit run app.py
-The application will launch in your default web browser, displaying the user interface.
-Load multiple PDF documents into the app by following the provided instructions.
-Ask questions in natural language about the loaded PDFs using the chat interface.

##Output
![output](https://github.com/user-attachments/assets/9dbfdc06-a6de-4578-b275-fbbcf9381f71)


