import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings, HuggingFaceInstructEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain_community.llms import HuggingFaceHub
from transformers.pipelines import pipeline
from langchain.llms import HuggingFacePipeline




import sys
import torch



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000.,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
 #embeddings = OllamaEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    # Create pipeline
    hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-xxl", max_length=512, temperature=0.5)

    # Wrap with LangChain
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
     


def handle_userinput(user_question):
    # 🛡️ Check if conversation chain exists
    if "conversation" not in st.session_state or st.session_state.conversation is None:
        st.error("Conversation not initialized. Please upload and process a PDF first.")
        return

    # ✅ FIXED: Call the conversation chain with a dictionary
    response = st.session_state.conversation({"question": user_question})

    # 🧠 Save chat history
    st.session_state.chat_history = response['chat_history']

    # 💬 Display messages
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


 
 


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    # Initialize session state variables
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    
    user_question = st.text_input("Ask a question about your documents:")
    
    # ✅ Prevent error if user asks question before uploading PDFs
    if user_question and st.session_state.conversation:
        handle_userinput(user_question)
    elif user_question and not st.session_state.conversation:
        st.warning("Please upload and process your PDFs first.")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                # Step 1: Extract text from PDFs
                raw_text = get_pdf_text(pdf_docs)

                # Step 2: Split into chunks
                text_chunks = get_text_chunks(raw_text)

                # Step 3: Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Step 4: Build the conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
if __name__ == '__main__':
    main()