import os

import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


def main():
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    st.set_page_config('PDF CHAT')
    st.header("Upload Your PDF,and Chat With PDF💬")
    st.text('Made By manoj Hp')

    # upload the Pdf
    pdf = st.file_uploader('Upload Your PDF here', type='pdf')

    # reading the pdf
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for pages in pdf_reader.pages:
            text += pages.extract_text()

        # split into Chunks
        splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunk = splitter.split_text(text)

        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunk, embeddings)

        # user input
        user_input = st.text_input('Ask any questions about your PDF')
        if user_input:
            docs = knowledge_base.similarity_search(user_input)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_input)

            st.write(response)


if __name__ == '__main__':
    main()
