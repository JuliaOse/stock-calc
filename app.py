import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

st.title("📈 Investment Profit Calculator")

symbol = st.text_input("Stock Symbol (e.g. AAPL)")
amount = st.number_input("Amount Invested", min_value=1.0)
date = st.date_input("Start Date")

def get_price_on_or_after(symbol, date):
    next_date = date + timedelta(days=3)
    data = yf.Ticker(symbol).history(start=date, end=next_date)
    if data.empty:
        return None, None
    row = data.iloc[0]
    return row.name.date(), row["Close"]

if st.button("Calculate"):
    actual_date, start_price = get_price_on_or_after(symbol, date)
    
    if start_price is None:
        st.error("No data found for that date.")
    else:
        current_price = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]
        shares = amount / start_price
        current_value = shares * current_price
        profit = current_value - amount

        st.subheader("Result")
        st.write(f"**Actual trading date:** {actual_date}")
        st.write(f"**Start price:** ${start_price:.2f}")
        st.write(f"**Current price:** ${current_price:.2f}")
        st.write(f"**Shares bought:** {shares:.4f}")
        st.write(f"**Value today:** ${current_value:.2f}")
        st.write(f"**Profit:** ${profit:.2f}")

        # Chart
        data = yf.Ticker(symbol).history(start=date)
        data["Value"] = data["Close"] * shares

        st.subheader("Growth Chart")
        st.line_chart(data["Value"])
