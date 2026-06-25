# 📰 Does Bad News = Bad Stock?

An AI app that analyzes financial news headlines 
and predicts stock movement using FinBERT.

## 🎯 What it does
- Takes a financial news headline as input
- Uses FinBERT AI to detect if sentiment is Positive/Negative/Neutral
- Fetches real stock price data from NSE
- Checks if AI prediction matched actual stock movement

## 🛠️ Tech Stack
- Python 3.14
- FinBERT (HuggingFace Transformers)
- yfinance (Real stock data)
- Streamlit (Web app)

## ▶️ How to Run
pip install transformers yfinance streamlit torch
streamlit run app.py

## 📊 Example
- Headline: "Infosys cuts revenue forecast amid weak demand"
- AI Sentiment: Negative (96.84% confident)
- Stock Movement: +7.93%
- Learning: Markets sometimes price in bad news beforehand!

## 👩‍💻 Built by Anannya Sane
First AI project — built while learning AI in Finance!
