import yfinance as yf
import pandas as pd
import os

# list of stocks to download
stocks = ["AAPL", "MSFT", "AMZN", "GOOGL", "SPY"]

# create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

for stock in stocks:
    print(f"Downloading {stock}...")

    data = yf.download(stock, start="2015-01-01")

    file_path = f"data/{stock}.csv"

    data.to_csv(file_path)

    print(f"{stock} saved to {file_path}")

print("All data downloaded successfully.")