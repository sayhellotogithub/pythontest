# これまでの問題で作成したモジュール（API取得、データ処理、グラフ作成）を利用して、

# 週間天気予報のデータとグラフを表示する main 関数を作成せよ。

# 必要に応じて都道府県名をユーザに入力させたり、エラーハンドリングを加えてもよい。
import weather_api
import parse_weather_data
import plot_weather_forecast
import json
import logging

def main():
    
    # prefecture = input("都道府県名を入力してください: ").strip()
    prefecture="滋賀県"
    area_code=weather_api.get_area_code(prefecture)
    if area_code is not None:
        print(area_code)
        if area_code.isdigit():
            weather_data = weather_api.get_weather_forecast(area_code)
            print(json.dumps(weather_data, indent=2, ensure_ascii=False))


       
            df=parse_weather_data.parse_weather_data(weather_data,area_name=prefecture)
            if df is not None:
                   plot_weather_forecast.show_weather_graph(df)      
            else:
               logging.error("None")
               

if __name__ == '__main__':
    main()
