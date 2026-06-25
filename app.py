import streamlit as st
from sentiment import get_sentiment
from stock import get_price_change

st.title("📰 Does Bad News = Bad Stock?")
st.write("Enter a news headline and see if AI can predict stock movement!")

headline = st.text_input("📝 Enter a news headline:")
ticker = st.text_input("📈 Enter NSE stock ticker (e.g. INFY.NS, RELIANCE.NS):")
date = st.date_input("📅 Date of the news:")

if st.button("Analyze"):
    if headline and ticker:
        with st.spinner("Analyzing..."):

            # Sentiment
            label, score = get_sentiment(headline)

            # Stock movement
            before, after, change = get_price_change(ticker, str(date))

        st.subheader("🧠 AI Sentiment")
        if label == "positive":
            st.success(f"Positive 📈 ({score}% confident)")
        elif label == "negative":
            st.error(f"Negative 📉 ({score}% confident)")
        else:
            st.warning(f"Neutral 😐 ({score}% confident)")

        st.subheader("📊 Stock Movement Next Day")
        if before:
            st.write(f"Before: ₹{before} → After: ₹{after}")
            st.metric("Price Change", f"{change}%")

            st.subheader("✅ Was AI Correct?")
            if (label == "positive" and change > 0) or \
               (label == "negative" and change < 0):
                st.success("AI prediction matched reality! ✅")
            else:
                st.error("AI prediction did NOT match reality ❌")
        else:
            st.warning("Could not fetch stock data for that date.")
    else:
        st.warning("Please fill in all fields!")