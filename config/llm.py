import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


#model name
model_name="gemini-3.1-flash-lite"

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model=model_name, 
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )

try:
    test_llm=llm.invoke("How are you")
    print("LLM Integration test successful")
except:
    print("LLM is not integrated properly. Please check your API key and model name.")