# PDF RAG QA Bot ([View on Hugging Face Spaces](https://huggingface.co/spaces/ArjunJagdale/pdf-rag-qa-bot))

---

## Summary

[**Live Demo on Hugging Face Spaces**](https://huggingface.co/spaces/ArjunJagdale/pdf-rag-qa-bot)

This project is an interactive Retrieval-Augmented Generation (RAG) app that allows users to upload a PDF and ask questions about its contents. The app uses LangChain and Hugging Face models to intelligently retrieve relevant information from the document and generate accurate answers.

---

## 1. What we did

- Built a web app that lets users upload a PDF and ask any question about its content.
- The app automatically processes the PDF, splits it into chunks, embeds those for semantic search, and uses an LLM to synthesize natural-language answers from the most relevant text segments.
- Deployed the solution on Hugging Face Spaces for instant online access.

---

## 2. How

- **User uploads a PDF** and asks a question.
- The app loads the PDF and splits it into manageable text chunks using LangChain's `RecursiveCharacterTextSplitter`.
- Each chunk is embedded using a Sentence Transformers model for efficient semantic search (vector similarity).
- When the user asks a question, the app retrieves the most relevant chunks using FAISS vector search.
- A Hugging Face LLM (e.g., FLAN-T5) is prompted with the question and the retrieved context chunks to generate a final answer.
- All components are orchestrated with LangChain's RetrievalQA pipeline, and the interface is built with Gradio.

---

## 3. Tech stack used

- **[LangChain](https://github.com/langchain-ai/langchain)** (`langchain`, `langchain-community`, `langchain-text-splitters`): For document loading, splitting, embeddings, vector search, and LLM chains.
- **[Hugging Face Transformers](https://github.com/huggingface/transformers)**: For loading both embedding and language models.
- **[Sentence Transformers](https://www.sbert.net/)**: For generating semantic vector representations of text chunks.
- **[FAISS](https://github.com/facebookresearch/faiss)**: For fast vector similarity search.
- **[Gradio](https://github.com/gradio-app/gradio)**: For building the user-facing web app.
- **[PyPDF2](https://github.com/py-pdf/PyPDF2)**: For PDF parsing.

---

## 4. Screenshots

**Resume Check:**

![Screenshot 2025-06-30 154937](https://github.com/user-attachments/assets/066b8c0d-392c-4c9e-95e3-e5ae4e64520a)

**Project management PDF check:**

![image](https://github.com/user-attachments/assets/a2c839dc-fb3e-4e7d-a5f7-259ebaa59c3e)

![image](https://github.com/user-attachments/assets/0a8ffd14-7077-4c2b-9ee5-e02e15d745cf)






---

Enjoy asking questions about your PDFs!
