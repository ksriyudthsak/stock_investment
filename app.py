import streamlit as st
import requests

st.title("My Stock Investment")

st.text("This is a stock investment app")

st.sidebar.write("This is a sidebar")

option = st.sidebar.selectbox("Which option?", ("trend", "news","tweepy"))

st.header(option)

if option == 'trend':
    st.subheader("This is a trend page")


