import gradio as gr
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline as hf_pipeline

def qa_on_pdf(pdf_file, question):
    try:
        # Load and split document
        loader = PyPDFLoader(pdf_file.name)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_docs = splitter.split_documents(docs)
        # Embedding model and vectorstore
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectordb = FAISS.from_documents(split_docs, embeddings)
        retriever = vectordb.as_retriever()
        # LLM for answer synthesis
        HF_TOKEN = os.getenv("HF_TOKEN")
        llm_pipe = hf_pipeline("text2text-generation", model="google/flan-t5-base", token=HF_TOKEN)
        llm = HuggingFacePipeline(pipeline=llm_pipe)
        # RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
        answer = qa_chain.run(question)
        return answer
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=qa_on_pdf,
    inputs=[gr.File(label="Upload PDF"), gr.Textbox(label="Question")],
    outputs="text",
    title="Ask Questions About Your PDF (LangChain v0.3 RAG Demo)"
)

if __name__ == "__main__":
    iface.launch()