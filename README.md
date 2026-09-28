# AI Scam Detection

A Streamlit proof of concept for exploring how an LLM can help people assess suspicious messages before they act.

## Problem

Scam messages often mimic routine communications: parcel updates, prize notifications, payment requests, or account alerts. A recipient needs a fast, understandable first-pass assessment—not an opaque binary verdict.

## Target User

Individuals who receive an unexpected message and want help identifying possible scam signals before clicking a link, sharing information, or making a payment.

## Solution

The app accepts a message and returns a structured assessment with:

- A classification: **Scam**, **Not a Scam**, or **Uncertain**
- A risk score from **0** to **5**
- A plain-language explanation of the detected signals
- A likely intent: **Financial**, **Phishing**, **Social Engineering**, or **Other**

The result is parsed against a Pydantic schema so the interface receives consistent fields rather than unstructured model text.

## User Flow

1. Select a prompt approach: **ReAct Prompt** or **Few Shot Prompt**.
2. Paste or type the message to assess.
3. Select **Predict Scam**.
4. Review the classification, risk score, explanation, and intent type.

## Prompt-Design Comparison

The interface makes prompt design observable rather than hiding it behind one model output.

| Approach | Product intent | How it guides the model |
| --- | --- | --- |
| ReAct Prompt | Make key risk checks explicit | Directs the model to consider urgency, payment requests, credential requests, suspicious links, and prizes before returning structured output. |
| Few Shot Prompt | Ground behavior in representative examples | Shows examples of financial fraud, a benign class update, and an ambiguous delivery-link message. |

This is a qualitative comparison tool. It does not claim a measured accuracy or superiority for either prompt approach.

## Product Decisions

- **Three-way classification:** `Uncertain` avoids forcing a confident safe-or-scam decision when the message needs independent verification.
- **Risk score plus explanation:** Gives users an interpretable reason to pause, instead of relying on a label alone.
- **Intent taxonomy:** Separates common harm patterns to make the outcome easier to understand.
- **Structured output:** Constrains the model response to fields the UI can reliably display.
- **Side-by-side prompt choice:** Enables lightweight experimentation with two prompting strategies in the same workflow.

## Limitations

- This is an educational prototype, not a production fraud-detection system.
- LLM outputs can be incorrect, incomplete, or overly confident.
- The app evaluates message text only; it does not validate senders, domains, URLs, attachments, transaction context, or external threat intelligence.
- A score or classification should not replace independent verification through official channels.
- No performance metrics are reported because this repository does not include a labelled evaluation dataset or benchmark.

## Demo

_Demo recording or screenshots to be added._

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
└── requirements.txt    # Python dependencies
```

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Pydantic
