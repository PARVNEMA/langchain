from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import sqlite3
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0.5)
def run_query(query,db):
  conn=sqlite3.connect(db)
  curr=conn.cursor()
  curr.execute(query)
  rows=curr.fetchall()
  conn.commit()
  conn.close()
  return rows

prompt= PromptTemplate(template='you are an expert in converting natural language to sql queries,the sql database has the table student with the columns name,class,section,roll_number,can you also the sql query should not have ``` in the end and beggining or the sql word in the output  generate sql query for {query}',input_variables=['query'])

st.set_page_config(page_title="Sql Project", page_icon=":tada:")
st.header("Gemini App to Retreive Sql data ")

question = st.text_input("Ask your Question:")

submit=st.button("Submit")

parser= StrOutputParser()
if submit :
  response=prompt | llm | parser
  original_quesion =response.invoke(question)
  st.write(original_quesion)
  data=run_query(original_quesion,"student.db")
  st.subheader("Results")
  for row in data:
    print(row)
    st.write(row)