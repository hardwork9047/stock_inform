import yfinance as yf


def get_stock_price(symbols):
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            price = stock.info.get("regularMarketPrice")

            if price is not None:
                print(f"{symbol}: ${price}")
            else:
                print(f"Unable to retrieve price for {symbol}.")
        except Exception as e:
            print(f"Error retrieving data for {symbol}: {e}")


if __name__ == "__main__":
    companies = ["MSFT", "AAPL"]  # MicrosoftとAppleの株式シンボル
    get_stock_price(companies)
