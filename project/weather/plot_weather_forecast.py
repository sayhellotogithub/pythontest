# matplotlib ライブラリを利用して、週間気温予報の最高気温・最低気温をグラフ化し、表示する関数 plot_weather_forecast を作成せよ。

# グラフは以下の条件を満たすように作成すること。

# また、問題１、２で作成したモジュールを利用して、東京都の週間気温予報のグラフを表示せよ。

# 条件
# グラフタイトル：あり
# ラベル：あり
# 凡例：あり
# 縦軸：温度、横軸：日付
# グラフ種別：折れ線グラフ
# 最高気温：赤 最低気温：青
import matplotlib.pyplot as plt
import parse_weather_data as parse_weather_data
import weather_api as weather_api

def show_weather_graph(df):
  
    df['最高気温(℃)'].fillna(0, inplace=True)
    df['最低気温(℃)'].fillna(0, inplace=True)
    print(df)

    # 折れ線グラフ作成
    # plt.rc('font', family='IPAexGothic')
    # 日本語フォントを設定
    # plt.rcParams['font.sans-serif'] = ['MS Gothic']  # 例えばMS Gothic
    # plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の表示問題を解決

    plt.figure(figsize=(10, 5))
    plt.plot(df['日付'], df['最高気温(℃)'], marker='o', color='red', label='最高気温')
    plt.plot(df['日付'],df['最低気温(℃)'],marker='*',color='blue',label="最低気温")
    plt.title('東京都の週間気温予報のグラフ')
    plt.xlabel('日付')
    plt.ylabel('温度 (°C)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    area_name="東京都"
    tokyo_code = weather_api.get_area_code("東京都")
    print(f"東京都のエリアコード: {tokyo_code}")
    
    if tokyo_code.isdigit():
        tokyo_weather = weather_api.get_weather_forecast(tokyo_code)
        # print(json.dumps(tokyo_weather, indent=2, ensure_ascii=False))
        df=parse_weather_data.parse_weather_data(tokyo_weather,area_name)
        show_weather_graph(df)
       
       
       
#                           日付 最高気温(℃) 最低気温(℃)
# 0  2025-02-26T00:00:00+09:00    None    None
# 1  2025-02-27T00:00:00+09:00      16       5
# 2  2025-02-28T00:00:00+09:00      18       3
# 3  2025-03-01T00:00:00+09:00      19       4
# 4  2025-03-02T00:00:00+09:00      22       8
# 5  2025-03-03T00:00:00+09:00      15       6
# 6  2025-03-04T00:00:00+09:00       8       3


