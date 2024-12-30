.. _STU(DYING):

.. title:: STU(DYING): AI-Powered Study Assistant

.. raw:: html

   <h1>
       <span style="color: #45364e;">STU(DYING): AI-Powered Study Assistant</span>
   </h1>

*Overview*
------------
STU(DYING) is a versatile Streamlit application that assists students with studying through AI-driven chatbots and flashcard generation. It processes PDF files to extract meaningful content and generates Q&A pairs for efficient learning. The app offers:

1. *Chatbot Mode*: Interactive question-answering capabilities.
2. *Flashcards Mode*: Automated Q&A extraction from PDFs.

*Prerequisites*
-----------------
.. raw:: html

   <h3>
       <span style="color: #45364e;">1. Python Environment</span>
   </h3>

Python 3.9 or newer.

.. raw:: html

   <h3>
       <span style="color: #45364e;">2. Required Libraries</span>
   </h3>

.. code-block:: bash

   pip install streamlit langdetect pdfplumber deep-translator

*Importing Libraries*
------------------------
.. code-block:: python

    import streamlit as st
    import io
    import re
    from appst import retriever, retrieve_from_db, get_chatbot_response, read_pdf
    from essai import extract_text_and_metadata, split_text_into_chunks, get_qa_from_nvidia_chat

*Setting Up the Application*
------------------------------
.. code-block:: python

    # Configure the app
    st.set_page_config(page_title="STU(DYING)", layout="centered")
    st.markdown("<h1 style='color: #45364e;'>STU(DYING)</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #829ded;'>Stu(Dying): Turning Stress into Success!</h3>", unsafe_allow_html=True)

*Menu Options*
-----------------
.. code-block:: python

    # Sidebar menu
    menu = ["Chatbot🤖", "Flashcards"]
    choice = st.sidebar.selectbox("Choose an option", menu)

*Chatbot Mode*
-----------------
.. code-block:: python

    if choice == "Chatbot🤖":
        st.subheader("Welcome to Stu(Dying): Your Study Buddy Chatbot!")
        file = st.file_uploader("Upload a PDF file", type=["pdf"])
        
        if file:
            # Process uploaded PDF
            doc = read_pdf(file)
            question = st.text_input("Ask a question")
            if st.button("Ask"):
                answer = retriever(doc, question)
                st.write(answer)
        else:
            question = st.text_input("Ask a question")
            if st.button("Ask"):
                answer = retrieve_from_db(question)
                st.write(answer)

*Flashcards Mode*
--------------------
.. code-block:: python

    elif choice == "Flashcards":
        st.subheader("Stu(dying): Power Up Your Knowledge, One Flashcard at a Time!")

        def main():
            st.title("PDF to Q&A Converter")
            st.write("Upload a PDF file to extract and format Q&A pairs.")

            uploaded_file = st.file_uploader("Upload PDF", type="pdf")
            if uploaded_file:
                pdf_content = extract_text_and_metadata(uploaded_file)
                st.write("Processing uploaded PDF...")

                # Combine text into a single string
                all_text = " ".join([page['text'] for page in pdf_content if 'text' in page and page['text']])

                # Split text into chunks
                chunks = split_text_into_chunks(all_text)
                st.write(f"Total chunks of text: {len(chunks)}")

                # Process each chunk
                formatted_output = []
                for i, chunk in enumerate(chunks):
                    st.subheader(f"Chunk {i + 1}")
                    st.write("Generating Q&A...")
                    qa_response = get_qa_from_nvidia_chat(chunk)
                    st.text_area(f"Q&A - Chunk {i + 1}", qa_response, height=200)

                    # Extract Q&A pairs
                    qa_pairs = re.findall(r'\\*Q\d+:\\\s(.?)\n\\*A\d+:\\\s(.?)(?:\n|$)', qa_response, re.DOTALL)
                    for question, answer in qa_pairs:
                        formatted_output.append(f"Question: {question}\tAnswer: {answer}")

                # Downloadable output
                output_text = "\n".join(formatted_output)
                output_file = io.StringIO(output_text)
                st.download_button(
                    label="Download Q&A File",
                    data=output_file.getvalue(),
                    file_name="qa_output.txt",
                    mime="text/plain",
                )

            main()

*Conclusion*
--------------
