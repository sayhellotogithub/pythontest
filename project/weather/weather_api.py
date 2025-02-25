import requests
import json

def get_area_code(prefecture_name: str) -> str:
    """
    気象庁APIから都道府県名に対応するエリアコードを取得する関数。
    
    :param prefecture_name: 都道府県名（例: "東京都"）
    :return: エリアコード（例: "130000"）
    """
    url = "https://www.jma.go.jp/bosai/common/const/area.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # for code,item in data.items():
        #     for code, info in item.items():
        #         print(info)
        #         if prefecture_name in info.get("name"):
        #             return code
        offices=  data.get("offices","{}")
        for code, info in offices.items():
            if prefecture_name in info.get("name"):
                return code

            
        return "該当する都道府県が見つかりません"
    except requests.RequestException as e:
        return f"エラーが発生しました: {e}"

def get_weather_forecast(area_code:str)->dict:
    url=f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

    try:
        response =requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"error:{e}"

if __name__ == "__main__":
    tokyo_code = get_area_code("沖縄")
    print(f"東京都のエリアコード: {tokyo_code}")
    
    if tokyo_code.isdigit():
        tokyo_weather = get_weather_forecast(tokyo_code)
        print(json.dumps(tokyo_weather, indent=2, ensure_ascii=False))
