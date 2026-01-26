import streamlit as st

st.header("Hello world")
title = st.text_input("Movie title", "")

# st.write("The current movie title is", title)

if(title):
  st.write("You selected:", title)