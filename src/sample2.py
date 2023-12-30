import yfinance as yf
from pandas_datareader import data as pdr
import datetime


# 指定したコードと期間でデータを取得をします。
# ticker → 個別株・指数のコード
# 　　start → 取得したい初めの日付
# 　　end  → 取得したい終わりの日付

ticker = "^N225"
start = datetime.date(1980, 1, 1)
# 翌日の日付を指定しないと当日の日付までのデータを取得できないので、翌日を指定しています
end = datetime.datetime.now() + datetime.timedelta(days=1)

# 日付を指定したい場合は↓の書き方。
# もし日付を変える場合は1日後を指定してください（5日まで取得したかったら6日を指定）
# 下記だと7月19日まで取得
# end =  datetime.date(2023,7,20)


# 日本個別株を取得する場合はコードの番号.Tを末尾につける必要があります。
# 例えばホクトの場合・・↓
# ticker = "1379.T"


# yfinanceのライブラリで指定した条件でデータを取得
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start, end)

# csvで保存
# ファイル名は上記tickerで指定した文字列_daily_data.csvとして保存されます
# 日経２２５の場合は　^N225_daily_data.csv　として保存されます。
# 保存したファイルの保存の仕方は こしかけ　の　noteで説明します。
df.to_csv(ticker + "_daily_data.csv", encoding="utf8")
