.. _Stu(dying):

.. title:: Stu(dying)
.. raw:: html

   <h1>
       <span style="color: #E0B0FF;">Chatbot🤖</span>
   </h1>

**Outline**
-----------

The chatbot is designed to provide instant, context-aware responses based on the content of uploaded PDFs.
Here's a simple demo showcasing how the chatbot was built, highlighting the steps , model integration, and creating the user interface.

**Prerequisites**
-----------------
.. raw:: html

   <h3>
       <span style="color: #45364e;">1. Python Environment</span>
   </h3>

Python 3.9 or newer.

.. raw:: html

   <h3>
       <span style="color: #45364e;">2. Required Python Libraries</span>
   </h3>

.. code-block:: bash

   pip install streamlit pdfplumber PyPDF2 langdetect langchain-community langchain-openai chromadb

.. raw:: html

   <h3>
       <span style="color: #45364e;">3. Ollama API</span>
   </h3>

* Download Ollama
* Download Required Models
.. code-block:: bash

    ollama pull llama3.2
    ollama pull mxbai-embed-large:latest


**Importing libraries**
------------------------
.. code-block:: python

    import streamlit as st
    import os 
    import PyPDF2
    import ollama
    import pdfplumber
    from langdetect import detect
    from langchain_community.vectorstores import Chroma
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_community.chat_models import ChatOllama
    from langchain_community.embeddings.ollama import OllamaEmbeddings
    from langchain_openai import ChatOpenAI
    from langchain.schema import Document
    from langchain.text_splitter import CharacterTextSplitter

**Reading the PDF file**
------------------------
.. code-block:: python

    def read_pdf(file):
    pdfReader = PyPDF2.PdfReader(file)
    all_page_text = ""
    for page in pdfReader.pages:
        all_page_text += page.extract_text() + "\n"
    return all_page_text

**Retrieve and respond to queries from a PDF file**
---------------------------------------------------
.. code-block:: python

    def retriever(doc, question):
    model_local = ChatOllama(model="llama3.2")

    doc = Document(page_content=doc)
    doc = [doc]
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=800, chunk_overlap=0)
    doc_splits = text_splitter.split_documents(doc)

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OllamaEmbeddings(model="mxbai-embed-large:latest"),
    )
    retriever = vectorstore.as_retriever(k=2)
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    if there is no answer, please answer with "I m sorry, the context is not enough to answer the question."
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model_local
        | StrOutputParser()
    )

    return after_rag_chain.invoke(question)

The model used in the retriever function is ChatOllama, specifically the **"llama3.2"** variant.
It is a conversational AI model,introduced by Meta in 2024, designed to process and generate human-like responses based on input prompts.
In this function, it serves as the final step in generating answers to questions, leveraging the context retrieved from a vector store.

**Additional Models Embedded:**

**"mxbai-embed-large"** is an embedding model used to convert the text from the documents into numerical vectors for similarity comparisons


**Generate Chatbot response with language detection**
-----------------------------------------------------
.. code-block:: python

    def get_chatbot_response(prompt):
    
    detected_language = detect(prompt)
    
    # Modify the prompt based on detected language
    if detected_language == 'fr':
        modified_prompt = "Veuillez répondre en français: " + prompt
    else:
        modified_prompt = prompt  # Default to English if language is not French
    
    # Call Ollama's API with the modified prompt
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": modified_prompt}])
    
    # Assuming the response is a dictionary-like object, get the text from the response
    return response['text']
    







        