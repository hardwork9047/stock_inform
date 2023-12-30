import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime

# テスラの株式コード
ticker = "TSLA"

# 過去1年間のデータを取得
end = datetime.datetime.now()
start = end - datetime.timedelta(days=365)

# yfinanceを使用してデータを取得
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start, end)

# 移動平均線の計算
df["MA10"] = df["Adj Close"].rolling(window=10).mean()
df["MA50"] = df["Adj Close"].rolling(window=50).mean()
df["MA200"] = df["Adj Close"].rolling(window=200).mean()

# プロット
plt.figure(figsize=(12, 6))
plt.plot(df["Adj Close"], label="TSLA")
plt.plot(df["MA10"], label="10-move-ave.")
plt.plot(df["MA50"], label="50-move-ave.")
plt.plot(df["MA200"], label="200-move-ave.")
plt.title("tsla")
plt.xlabel("date")
plt.ylabel("value")
plt.legend()
plt.show()
# プロットをファイルに保存
plt.savefig("tesla_stock_price.png")
