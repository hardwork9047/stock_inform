def fourth_order_diff(series):
    """
    4次精度の中心差分を計算する関数。
    :param series: 差分を計算するPandas Series
    :return: 4次精度の中心差分が計算されたSeries
    """
    d1 = series.shift(-2)  # 2つ後の値
    d2 = series.shift(-1)  # 1つ後の値
    d3 = series.shift(1)  # 1つ前の値
    d4 = series.shift(2)  # 2つ前の値
    # print(f"series:{series}")
    # print(f"d1:{d1}")
    return (-d4 + 8 * d3 - 8 * d2 + d1) / 12
