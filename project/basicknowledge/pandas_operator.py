import pandas as pd

# data =[10,20,30,40]
# series= pd.Series(data,index=['a','b','c','d'])
# print(series)

# Series
#行と列を持つ表形式データ。
# Excelの表をPythonで扱うイメージ。
data = {
    '名前': ['田中', '山田', '鈴木'],
    '年齢': [25, 30, 35],
    '得点': [90, 85, 80]
}
df = pd.DataFrame(data)
# print(df)

# print(df.head())  # 上位5行
# print(df.tail(2))  # 下位2行
# print(df.info())  # データ概要
# print(df.describe())  # 統計情報
print(df['名前'])  # 列の選択
print(df.loc[0])  # 行の選択（ラベルベース）
print(df.iloc[1])  # 行の選択（インデックスベース）
