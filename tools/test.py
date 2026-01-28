from langchain_community.tools import DuckDuckGoSearchResults
import streamlit as st


# 🔍 Why this happens

# DuckDuckGoSearchResults is a class, not an instance.

# In LangChain:

# invoke() is an instance method

# It expects self + input

# You’re calling it directly on the class, so self is missing → 💥 error
st.title("DuckDuckGo Search Results :heart:")


input = st.text_input("Search query")

if(input !=""):
  tool = DuckDuckGoSearchResults()
  results=tool.invoke(input)
  print(results)
  st.write(results)
