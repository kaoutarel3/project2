.. project2 documentation master file, created by
   sphinx-quickstart on Thu Dec  5 22:47:41 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Stu(dying)
======================
This project leverages Streamlit to develop an interactive platform where users can upload PDF documents.
======================
The system processes the PDF to automatically generate flashcards, aiding in the extraction and memorization of key information. 
======================
Additionally, a chatbot is integrated to provide on-demand, context-driven responses based on the content of the uploaded PDF,
======================
facilitating efficient information retrieval and enhancing the user learning experience.😁

======================
**Building the chatbot**
======================

We used Ollama models and embedding to create a streamlit app capable of answering questions on the uploaded pdf document.

======================
**The models used**
======================

*llama3.2:*
======================
-Llama 3.2 is a language model introduced by Meta in 2024, featuring a variety of model sizes to suit different needs.
======================
*mxbai-embed-large:*
======================
-it was trained with no overlap of the MTEB data, which indicates that the model generalizes well across several domains, tasks and text length, in embedding your dataset
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

