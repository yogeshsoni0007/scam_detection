# To write the code in new file app.py

# Need to import the required libraries
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

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
    st.write("LLM Integration test successful")
except:
    st.write("LLM is not integrated properly. Please check your API key and model name.")


class ScamIntentResponse(BaseModel):
    category: Literal["Scam", "Not a Scam", "Uncertain"]
    risk_score:int=Field(ge=0, le=5)
    reasoning:str
    intent_type:Literal["Financial", "Phishing", "Social Engineering", "Other"]

parser = PydanticOutputParser(pydantic_object=ScamIntentResponse)


#Prompts 
## ReAct Prompt 
react_prompt=ChatPromptTemplate.from_template(
"""
You are an advanced AI Scam Detector, your role is to detect whether the incoming user message is Scam or not

Follow this ReAct Process before givign the final answer:
Thought: Identify the important claims and possible scam signals in the message
Action: Check for urgency, payment requests, OTP/password requests, suspicious links, suspicious prizes, lottery
Observation: Decide whether the signal is strongly indicating a scam, or not a scam or harmless.
Final answer: Fill the required structured output

Do give your reasoning behind it and explain the risk attached to it
{format_instructions}
Message:{message}
""")

#Few shot Prompt
few_shot_prompt=ChatPromptTemplate.from_template(
"""
You are an advanced AI Scam Detector, your role is to detect whther the incoming user message is Scam or not
Learn from the examples below and then classify the message

Example 1
Message: Congratulations! You have won ₹10 Lakhs. Pay a small processing fee to claim your prize.
Category: Scam
Risk score: 5
Reasoning: An unexpected prize with an upfront payment request is a common financial fraud pattern.
Intent type: Financial Fraud

Example 2
Message: Hi students, tomorrow's class will start at 10 AM in Room 201.
Category: Not Scam
Risk score: 0
Reasoning: This is a normal class update with no harmful request.
Intent type: Other

Example 3
Message: Your parcel is waiting. Click this link to track it.
Category: Uncertain
Risk score: 3
Reasoning: It could be genuine, but an unexpected link should be verified through the courier's official website.
Intent type: Phishing


Do give your reasoning behind it and explain the risk attached to it
{format_instructions}
Message:{message}
""")

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





