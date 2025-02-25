# # 問題２
# pandas ライブラリを利用して、以下の関数を作成せよ。

# また、問題１で作成したモジュール weather_api.py を利用して、東京都の週間気温予報を表として出力せよ。

# （取得時間によって一部のデータが入っていない場合もある。）

# 関数①
# 天気予報（JSON）から週間気温予報を抽出し「日付ごとの最高気温・最低気温」を整理する関数 parse_weather_data を作成せよ。

# JSONデータ構造
# 今回必要になる簡易データ構造を下記に示す。元データは問題１のものを確認すること。

# [
#     {
#         "timeSeries": [
#             ...(省略)...
#         ]
#     },
#     {   // 週間予報
#         "timeSeries": [
#             {   // 週間予報
#                 ...(省略)...
#             },
#             {   // 週間気温予報
#                 "timeDefines": ["2025-02-11T00:00:00+09:00", "2025-02-12T00:00:00+09:00", "2025-02-13T00:00:00+09:00", "2025-02-14T00:00:00+09:00", "2025-02-15T00:00:00+09:00", "2025-02-16T00:00:00+09:00", "2025-02-17T00:00:00+09:00"],
#                 "areas": [
#                     {
#                         "area": {"name": "東京", "code": "44132"},
#                         "tempsMin": ["", "1", "4", "2", "3", "4", "4"],
#                         "tempsMax": ["", "13", "13", "14", "13", "15", "12"],
#                     },
#                     ...(省略)...
#                 ]
#             },
#         ]
#     }
# ]
# 作成後、コードの先頭に以下を記載して実行し、ファイルを作成しておくこと。

import pandas as pd
import weather_api as weather_api
import json

def parse_weather_data(weather_json,area_name):

    # for timeSerieItem in weather_json[1]['timeSeries']
    time_series=weather_json[1]['timeSeries'][1]
    print(time_series)
    dates= time_series['timeDefines']
    areas= time_series['areas']

    tokyo_data=next((area for area in areas if area['tempsMin'] is not None),None)
    if tokyo_data!=None:

        temps_min= tokyo_data['tempsMin']
        temps_max=tokyo_data['tempsMax']

        data=[]
        for date,min_temp,max_temp in zip(dates,temps_min,temps_max):

            data.append([date,max_temp if max_temp!="" else None,min_temp if min_temp!="" else None])

        # DataFrame 作成
        df=pd.DataFrame(data,columns=['日付','最高気温(℃)','最低気温(℃)'])
        return df
    else:
        return None

def parse_weather_data_new(weather_json,area_name):
    time_series=weather_json[1]['timeSeries'][1]
    print(time_series)

    dates= time_series['timeDefines']
    areas= time_series['areas']

    tokyo_data=next((area for area in areas if area['area']['name']==area_name ),None)
    if tokyo_data!=None:

        temps_min= tokyo_data['tempsMin']
        temps_max=tokyo_data['tempsMax']

        data=[]
        for date,min_temp,max_temp in zip(dates,temps_min,temps_max):

            data.append([date,max_temp if max_temp!="" else None,min_temp if min_temp!="" else None])

        # DataFrame 作成
        df=pd.DataFrame(data,columns=['日付','最高気温(℃)','最低気温(℃)'])
        return df
    else:
        return None
if __name__ == "__main__":
    area_name="東京都"
    tokyo_code = weather_api.get_area_code("東京都")
    print(f"東京都のエリアコード: {tokyo_code}")
    
    if tokyo_code.isdigit():
        tokyo_weather = weather_api.get_weather_forecast(tokyo_code)
        # print(json.dumps(tokyo_weather, indent=2, ensure_ascii=False))

        print(parse_weather_data(tokyo_weather,area_name))
       
#                           日付 最高気温(℃) 最低気温(℃)
# 0  2025-02-26T00:00:00+09:00    None    None
# 1  2025-02-27T00:00:00+09:00      16       5
# 2  2025-02-28T00:00:00+09:00      18       3
# 3  2025-03-01T00:00:00+09:00      19       4
# 4  2025-03-02T00:00:00+09:00      22       8
# 5  2025-03-03T00:00:00+09:00      15       6
# 6  2025-03-04T00:00:00+09:00       8       3