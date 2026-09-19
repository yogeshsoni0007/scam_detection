# AI Scam Detection

A Streamlit proof of concept that uses Google Gemini and LangChain to classify suspicious messages, score their risk, and explain the signals behind each prediction.

## What It Does

- Classifies a message as **Scam**, **Not a Scam**, or **Uncertain**
- Assigns a risk score from **0 to 5**
- Explains the reasoning behind the result
- Identifies the likely intent: **Financial**, **Phishing**, **Social Engineering**, or **Other**
- Lets users compare **ReAct** and **few-shot** prompting techniques
- Validates the model response with a Pydantic schema

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Pydantic

## Run Locally

1. Clone the repository and enter the project directory.

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example and add your Google API key:

```bash
cp .env.example .env
```

```env
GOOGLE_API_KEY=your_api_key
```

5. Start the application:

```bash
streamlit run src/app.py
```

## Project Structure

```text
scam_detection/
├── config/llm.py       # Gemini configuration
├── src/app.py          # Streamlit interface and inference flow
├── src/parser.py       # Structured response schema
├── src/prompts.py      # ReAct and few-shot prompts
├── data/               # Sample datasets
└── requirements.txt    # Python dependencies
```

## Key Learnings

This project explores how prompt design changes classification behavior, how structured output makes LLM responses reliable for applications, and how explainable risk signals can support scam-awareness workflows.

## Disclaimer

This is an educational prototype, not a production fraud-detection system. Predictions should not replace independent verification or professional advice.
