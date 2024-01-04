import os
import schedule
import time
import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime
import utility.line as line
import utility.calculate as cl

# from datetime import datetime, timedelta
import matplotlib.dates as mdates


def job():
    # テスラの株式コード
    ticker = "TSLA"

    # 過去1年間のデータを取得
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365)

    # yfinanceを使用してデータを取得
    yf.pdr_override()
    df = pdr.get_data_yahoo(ticker, start, end)

    # 移動平均線の計算
    df["MA5"] = df["Adj Close"].rolling(window=5).mean()
    df["MA10"] = df["Adj Close"].rolling(window=10).mean()
    df["MA25"] = df["Adj Close"].rolling(window=25).mean()
    df["MA50"] = df["Adj Close"].rolling(window=50).mean()
    df["MA200"] = df["Adj Close"].rolling(window=200).mean()

    df.to_csv(ticker + "_daily_data.csv", encoding="utf8")
    df["MA5"].to_csv(ticker + "_daily_data_MA5.csv", encoding="utf8")
    df["MA10"].to_csv(ticker + "_daily_data_MA10.csv", encoding="utf8")
    df["MA25"].to_csv(ticker + "_daily_data_MA25.csv", encoding="utf8")
    df["MA50"].to_csv(ticker + "_daily_data_MA50.csv", encoding="utf8")
    df["MA200"].to_csv(ticker + "_daily_data_MA200.csv", encoding="utf8")

    # 移動平均線の傾きの計算
    df["MA5_slope"] = cl.fourth_order_diff(df["MA5"])  # MA5の傾き
    df["MA10_slope"] = cl.fourth_order_diff(df["MA10"])  # MA10の傾き
    df["MA25_slope"] = cl.fourth_order_diff(df["MA25"])  # MA25の傾き
    df["MA50_slope"] = cl.fourth_order_diff(df["MA50"])  # MA50の傾き
    df["MA200_slope"] = cl.fourth_order_diff(df["MA200"])  # MA200の傾き
    df["MA5_slope"].to_csv(ticker + "_daily_data_MA5_slope.csv", encoding="utf8")
    df["MA10_slope"].to_csv(ticker + "_daily_data_MA10_slope.csv", encoding="utf8")
    df["MA25_slope"].to_csv(ticker + "_daily_data_MA25_slope.csv", encoding="utf8")
    df["MA50_slope"].to_csv(ticker + "_daily_data_MA50_slope.csv", encoding="utf8")
    df["MA200_slope"].to_csv(ticker + "_daily_data_MA200_slope.csv", encoding="utf8")

    # 最新の傾きを取得
    latest_MA5_slope = df["MA5_slope"].dropna().iloc[-1]
    latest_MA10_slope = df["MA10_slope"].dropna().iloc[-1]
    latest_MA25_slope = df["MA25_slope"].dropna().iloc[-1]
    latest_MA50_slope = df["MA50_slope"].dropna().iloc[-1]
    latest_MA200_slope = df["MA200_slope"].dropna().iloc[-1]

    print(f"MA5 slope: {latest_MA5_slope}")
    print(f"MA10 slope: {latest_MA10_slope}")
    print(f"MA25 slope: {latest_MA25_slope}")
    print(f"MA50 slope: {latest_MA50_slope}")
    print(f"MA200 slope: {latest_MA200_slope}")

    # プロットの準備
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 株価のプロット（第一y軸）
    ax1.plot(df["Adj Close"], label="TSLA", color="black")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Adj Close", color="black")
    ax1.tick_params(axis="y", labelcolor="black")

    # x軸の日付フォーマットを '年-月-日' に設定
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    # x軸の範囲を現在から3ヶ月前までに設定
    three_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)
    ax1.set_xlim(three_months_ago, datetime.datetime.now())

    # 移動平均線のプロット（第一y軸）
    ax1.plot(df["MA5"], label="5-move-ave.", linestyle="--", color="red")
    ax1.plot(df["MA10"], label="10-move-ave.", linestyle="--", color="purple")
    ax1.plot(df["MA25"], label="25-move-ave.", linestyle="--", color="blue")
    ax1.plot(df["MA50"], label="50-move-ave.", linestyle="--", color="green")
    # ax1.plot(df["MA200"], label="200-move-ave.", linestyle="--", color="darkgreen")
    # ax1.set_ylim(-200, 400)
    ax1.set_ylim(150, 300)

    # タイトルと凡例
    plt.title("TSLA Stock Price and Moving Averages")
    ax1.legend(loc="upper left")

    # # 第二y軸の作成
    # ax2 = ax1.twinx()

    # # 傾きのプロット（第二y軸）
    # ax2.plot(df["MA5_slope"], label="MA5 Slope", linestyle=":", color="red")
    # ax2.plot(df["MA10_slope"], label="MA10 Slope", linestyle=":", color="purple")
    # ax2.plot(df["MA25_slope"], label="MA10 Slope", linestyle=":", color="blue")
    # ax2.plot(df["MA50_slope"], label="MA50 Slope", linestyle=":", color="green")
    # # ax2.plot(df["MA200_slope"], label="MA200 Slope", linestyle=":", color="darkgreen")
    # ax2.set_ylabel("Slope", color="black")
    # ax2.tick_params(axis="y", labelcolor="black")

    # # 第二y軸の範囲を設定
    # ax2.set_ylim(-10, 50)
    # ax2.legend(loc="upper right")

    # 日付フォーマットの変更 (YYYYMMDD)
    start_str = start.strftime("%Y%m%d")
    end_str = end.strftime("%Y%m%d")

    # ディレクトリのパス
    directory = "runs"

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)

    # ファイル名を設定（ディレクトリパスを含む）
    filename = f"{directory}/{ticker}_stock_price_{start_str}_to_{end_str}.png"
    plt.savefig(filename)
    plt.show()

    # 最新から5日分のMA10とMA50のデータを取得し、比較結果を出力
    latest_MA5 = df["MA5"].iloc[-5:]
    latest_MA10 = df["MA10"].iloc[-5:]
    latest_MA25 = df["MA25"].iloc[-5:]
    latest_MA50 = df["MA50"].iloc[-5:]
    latest_dates = df.index[-5:]

    print("Comparing latest 5 days of MA10 and MA50:")
    messages = [f"TSLA ({start_str} - {end_str})[M5, M25, Diff]"]
    for i in range(5):
        date = latest_dates[i]
        ma5_value = latest_MA5.iloc[i]
        ma10_value = latest_MA10.iloc[i]
        ma25_value = latest_MA25.iloc[i]
        ma50_value = latest_MA50.iloc[i]
        comparison = (
            "⭐️" if ma5_value > ma25_value else "❎" if ma5_value < ma25_value else "🌥️"
        )
        # print(
        #     f"Date: {date}, MA10: {ma10_value:.2f}, MA50: {ma50_value:.2f}, Diff: {ma10_value - ma50_value:.2f}, Comparison: {comparison}"
        # )
        messages.append(
            f"{date:%m/%d},[{ma5_value:.0f}, {ma25_value:.0f}, {ma5_value - ma25_value:.0f}], {comparison}"
        )

    # LINE Notifyを通じて通知
    # line.send_line_notify(f"テスラの株価チャート ({start_str} - {end_str})", filename)
    line.send_line_notify(messages, filename)
    # line.send_line_notify_group(f"テスラの株価チャート ({start_str} - {end_str})", filename)


job()

# 毎朝7時に`job`関数を実行するようにスケジュールを設定
schedule.every().day.at("07:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
