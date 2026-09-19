from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


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