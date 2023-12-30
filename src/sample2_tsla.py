import yfinance as yf
from pandas_datareader import data as pdr

import datetime

# テスラの株式コード
ticker = "TSLA"

# 現在から1週間前の日付
start = datetime.datetime.now() - datetime.timedelta(days=7)
# 現在の日付
end = datetime.datetime.now()

# yfinanceのライブラリで指定した条件でデータを取得
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start, end)

# 平均値、中央値、標準偏差を計算
mean_price = df["Adj Close"].mean()
median_price = df["Adj Close"].median()
std_dev = df["Adj Close"].std()

# 結果の出力
print(f"平均値: {mean_price}")
print(f"中央値: {median_price}")
print(f"標準偏差: {std_dev}")
