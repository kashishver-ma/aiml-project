import os
from dotenv import load_dotenv
from langchain_community.llms import ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
##we can customise this clas
#ai msg and human msgpippip install streamlit

from langchain_core.output_parsers import StrOutputParser

#chatbot+api+project api

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]=True

os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the questions asked"),
    ("user", "question:{question}")
])

st.title("Langchain Demo with gamma model")
imput_text=st.text_input("What question do u have in mind?")

llm=ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))



