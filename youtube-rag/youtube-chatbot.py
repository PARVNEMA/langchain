from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

st.header("Youtube Chatbot")
## ? youtube transcript loading
video_id = st.text_input("Youtube video ID","") # only the ID, not full URL

if video_id:
      st.write(f"https://www.youtube.com/watch?v={video_id}")
      try:
        # If you don’t care which language, this returns the “best” one
          transcript_list = YoutubeLoader.from_youtube_url(youtube_url=video_id,add_video_info=False,)
          # print("transcript_list",transcript_list.load())
          transcript = transcript_list.load()
          # Flatten it to plain text
          # transcript = " ".join(chunk["page_content"] for chunk in loaded_transcript)
          print("transcript",transcript)

      except ValueError:
          print("No captions available for this video.")
          st.write("No captions available for this video.")


      if(video_id):
        question=st.text_input("Ask your Question:", "")

      ## ? text splitting of transcript
      splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
      chunks = splitter.create_documents([transcript[0].page_content])

      ## ? generating embedding of the splitted text
      embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
      vector_store = FAISS.from_documents(chunks, embeddings)

      ## ? retreive the documents based on queries
      retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})

      ## ? prompt template is formed
      prompt = PromptTemplate(
          template="""
            You are a helpful assistant.
            Answer ONLY from the provided transcript context.
            If the context is insufficient, just say you don't know.

            {context}
            Question: {question}
          """,
          input_variables = ['context', 'question']
      )

      ## ? document is formated for giving it in context
      def format_docs(retrieved_docs):
        context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
        return context_text

      if question:
          # parallel chain is called to give context and question to our LLM
          parallel_chain = RunnableParallel({
              "context": retriever | RunnableLambda(format_docs),
              "question": RunnablePassthrough()
          })

          parser = StrOutputParser()

          llm = ChatGoogleGenerativeAI(
              model="gemini-3-flash-preview",
              temperature=0.5,
          )

          # main chain
          main_chain = parallel_chain | prompt | llm | parser

          result = main_chain.invoke(question)

          print(result)
          st.write(result)
