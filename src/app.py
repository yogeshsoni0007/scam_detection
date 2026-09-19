import os
import streamlit as st
from prompts import *
from parser import *
from config.llm import llm

# Streamlit App building 
st.title("Scam Detector Application")
st.write("Enter a message below to check if it is a scam or not.")

prompt_type=st.radio("Select Prompt Technique", ("ReAct Prompt", "Few Shot Prompt"))
user_message=st.text_area("Enter your message here:")

if st.button("Predict Scam"):
    if user_message:
        if prompt_type=="ReAct Prompt":
            selected_chain=react_prompt | llm | parser
        else:
            selected_chain=few_shot_prompt | llm | parser

        predicted_result=selected_chain.invoke({
            "message": user_message,
            "format_instructions": parser.get_format_instructions()     
        })
        st.subheader("Prediction Result:")
        st.write("Category:", predicted_result.category)
        st.write("Risk Score:", predicted_result.risk_score)
        st.write("Reasoning:", predicted_result.reasoning)
        st.write("Intent Type:", predicted_result.intent_type)

    else:
        st.write("Please enter a message to analyze.")




