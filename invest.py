import argparse
import yfinance as yf
from rich.console import Console
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

console = Console()

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    if data.empty:
        return None
    return float(data["Close"].iloc[-1])

def get_price_on_or_after(symbol, date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    next_date = date + timedelta(days=3)

    stock = yf.Ticker(symbol)
    data = stock.history(start=date, end=next_date)

    if data.empty:
        return None, None

    actual_date = data.index[0].strftime("%Y-%m-%d")
    price = float(data["Close"].iloc[0])
    return actual_date, price

def calculate_investment(symbol, invested_amount, start_date):
    actual_date, start_price = get_price_on_or_after(symbol, start_date)

    if start_price is None:
        console.print("[red]No data found around that date.[/red]")
        return

    current_price = get_stock_price(symbol)
    shares = invested_amount / start_price
    current_value = shares * current_price
    profit = current_value - invested_amount

    console.print("\n[bold cyan]Investment Summary[/bold cyan]")
    console.print(f"[yellow]Symbol:[/yellow] {symbol}")
    console.print(f"[yellow]Requested Date:[/yellow] {start_date}")
    console.print(f"[yellow]Actual Trading Date:[/yellow] {actual_date}")
    console.print(f"[yellow]Start Price:[/yellow] ${start_price:.2f}")
    console.print(f"[yellow]Current Price:[/yellow] ${current_price:.2f}")
    console.print(f"[yellow]Shares Bought:[/yellow] {shares:.4f}")
    console.print(f"[yellow]Current Value:[/yellow] ${current_value:.2f}")
    console.print(f"[bold green]Profit:[/bold green] ${profit:.2f}")

    plot_stock_price(symbol, actual_date)
    plot_investment_value(symbol, invested_amount, actual_date)

def plot_stock_price(symbol, start_date):
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date)

    if data.empty:
        console.print("[red]No price data available for chart.[/red]")
        return

    plt.figure(figsize=(10,5))
    plt.plot(data.index, data["Close"])
    plt.title(f"{symbol} Stock Price Since {start_date}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_investment_value(symbol, invested_amount, start_date):
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date)

    if data.empty:
        console.print("[red]No data to plot investment growth.[/red]")
        return

    # Use Adjusted Close
    start_price = data["Close"].iloc[0]
    shares = invested_amount / start_price

    # Calculate investment value each day
    data["Value"] = data["Close"] * shares

    plt.figure(figsize=(10,5))
    plt.plot(data.index, data["Value"])
    plt.title(f"Value of ${invested_amount} Invested in {symbol} Since {start_date}")
    plt.xlabel("Date")
    plt.ylabel("Value (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(
        description="Calculate how much your investment would be worth today."
    )

    parser.add_argument("symbol", help="Stock ticker symbol (e.g., AAPL)")
    parser.add_argument("amount", type=float, help="Amount invested")
    parser.add_argument("date", help="Start date (YYYY-MM-DD)")

    args = parser.parse_args()
    calculate_investment(args.symbol, args.amount, args.date)

if __name__ == "__main__":
    main()
