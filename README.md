# 🎒 MissedTheBag

See how much money you could have made… if you didn’t miss the bag.  

**Live Demo:** [https://missedthebag.streamlit.app](https://missedthebag.streamlit.app)

---

## 🚀 Overview

**MissedTheBag** is a simple yet powerful stock investment calculator that lets you:

- See how much your money would be worth today if you had invested on a specific past date.  
- Find out the exact number of shares you would have bought.  
- Check your current profit or loss.  
- View historical stock price charts.  
- Track historical investment value over time.  

Built with **Python**, **Streamlit**, and **yfinance**, it turns market regret into clear, actionable insights.

---

## ✨ Features

### 📈 Investment Value Simulation

Simply enter:

- **Stock symbol** (e.g., AAPL, TSLA)  
- **Amount invested**  
- **Historical date**  

MissedTheBag calculates the real performance of your investment up to today.

### 🧮 Accurate Trading-Day Adjustment

If your chosen date falls on a weekend or market holiday, MissedTheBag automatically selects the next valid trading day.

### 📊 Beautiful Charts

- Historical stock price chart  
- Investment growth chart  

Both charts are rendered dynamically using **Streamlit** and **Matplotlib**.

### ⚡ API-Accurate Data

Powered by **yfinance**, fetching real historical and current market prices for precise calculations.

### 🖥️ Modern UI

Clean, interactive frontend built with **Streamlit** for easy exploration of your hypothetical investments.

---

## 🛠️ Tech Stack

| Layer      | Technology      |
|-----------|----------------|
| Frontend  | Streamlit       |
| Backend   | Python          |
| Data      | yfinance        |
| Charts    | Matplotlib      |
| Environment | Virtualenv / pip |

---

## 📦 Installation

1. Clone the repository:  
   ```bash
   git clone <repo-url>

2. Install the requirements

3. Run the app
    ```bash
    streamlit run app.py


##  Example Usage

Enter:

Symbol: AAPL

Amount: 1000

Date: 2020-01-02

MissedTheBag will calculate:

Trading date used

Starting price

Current price

Shares purchased

Current value

Total profit

Growth charts


## 🌍 Deployment

MissedTheBag is deployed on Streamlit Community Cloud, making it accessible to everyone.


## 👩🏽‍💻 Julia Osei
Built with love, Python, and some prompting.
