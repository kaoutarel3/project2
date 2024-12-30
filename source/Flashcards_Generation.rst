.. _Stu(dying):

.. title:: Stu(dying)
.. raw:: html

   <h1>
       <span style="color: #E0B0FF;">Flashcards</span>
   </h1>
**Outline**
-----------

The PDF to Q&A Converter is a Streamlit application designed to extract text from uploaded PDF files and generate context-aware Q&A pairs using an advanced AI model. This tool supports multi-language PDFs, automated chunking of text, and language translation for comprehensive usability.


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

   pip install streamlit pdfplumber langdetect deep-translator

.. raw:: html

   <h3>
       <span style="color: #45364e;">3. Ollama API</span>
   </h3>

* Download Ollama
* Pull the desired model

.. code-block:: bash

    ollama pull llama3.2

**Importing Libraries**
------------------------
.. code-block:: python

    import streamlit as st
    import pdfplumber
    import io
    import re
    from deep_translator import GoogleTranslator
    from langdetect import detect

**Reading the PDF File**
------------------------
.. code-block:: python

    def extract_text_and_metadata(pdf_file):
        """Extract text and metadata from a PDF file."""
        pdf_content = []
        try:
            pdf_file.seek(0)  # Reset the file pointer
            with pdfplumber.open(io.BytesIO(pdf_file.read())) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    page_data = {
                        'page_number': page_num + 1,
                        'text': text,
                    }
                    pdf_content.append(page_data)
        except Exception as e:
            st.error(f"Error extracting PDF content: {str(e)}")
        return pdf_content

**Splitting Text into Chunks**
------------------------------
.. code-block:: python

    def split_text_into_chunks(text, max_words=300):
        """Split text into smaller chunks with a maximum word count."""
        words = text.split()
        chunks = []
        current_chunk = []

        for word in words:
            if len(current_chunk) + 1 > max_words:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
            else:
                current_chunk.append(word)

        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks

**Detecting and Translating Language**
--------------------------------------
.. code-block:: python

    def detect_language(text):
        """Detect the language of the provided text."""
        try:
            detected_lang = detect(text)
            return detected_lang
        except Exception as e:
            return "en"  # Default to English if detection fails

    def translate_text(text, source_lang, target_lang):
        """Translate text from the source language to the target language."""
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            return translated
        except Exception as e:
            return f"Translation error: {str(e)}"

The application integrates AI-driven Q&A generation with language detection and translation, ensuring accessibility for users worldwide. The **"llama3:8b"** model is employed for contextual understanding and response generation.



