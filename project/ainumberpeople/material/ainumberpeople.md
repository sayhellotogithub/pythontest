#### 目標

AI数字人を活用したライブコマースは、24時間無休で商品を紹介したり、視聴者の質問にリアルタイムで答えたりすることができます

### 流れ

#### AI数字人の作成

* **Avatars（アバター）生成ツール**：D-ID、Synthesiaなどを使って、デジタルキャラクターを作成。
* 外見・声・話し方をブランドイメージに合わせてカスタマイズ。

#### シナリオ作成とデータ連携

* 商品紹介スクリプトを作成。
* AIチャットボットを組み込み、視聴者の質問に自動回答。
* 商品データベースと接続して、在庫状況・価格・特典をリアルタイム表示。

#### ライブ配信プラットフォームの選定

* **中国系プラットフォーム**：抖音（Douyin）、淘宝直播（Taobao Live）。

* **日本・グローバル系**：YouTube Live、Instagram Live、楽天ライブ。

#### AI音声＆動画合成

- AIにリアルタイムで話させるために、Text-to-Speech（TTS）技術を導入。
- OpenAIの「ChatGPT API」などを活用して、コメント対応を自動化。

#### 視聴者データ分析＆最適化

視聴者の反応や購買行動を追跡し、データに基づいてスクリプトやプロモーション戦略を改善。



### 開発流れ

#### OBS 

複数のソフトの画面を組み合わせたり、音声や音楽を統合して映像を撮影することができるソフトです。

Youtubeの生放送できます

#### VRoid Studio

動かすVTuberのモデル（姿）を用意

Live2d

VRMという形式の３Dモデルを使います。

#### Magic Mirror

VMagicMirrorはWindows PCでVRMアバターを表示し、特別なデバイスを使わずキャラクターを動かせるアプリケーションです。

#### 3teneFREE_beta

MacosでMagic Mirrorを使用することができないので、これの代わりに3teneFREE_betaを利用して、音声とか動きとかを実現しました。

#### VOICEVOX

これを利用して個性的なキャラクターの音声を使用することができます。

```python

import requests
import sounddevice as sd
import soundfile as sf
import os
import time
#pip install sounddevice scipy soundfile

def play_reply(comment,reply):
    params ={"text":f"{comment} {reply}","speaker":3}
    res= requests.post(f'http://127.0.0.1:50021/audio_query',params=params)
    res= requests.post(f'http://127.0.0.1:50021/synthesis',params=params,json=res.json())
    voice = res.content

    file_path = os.path.join(os.path.dirname(__file__), "material", "aituber-voice.wav")

    with open(file_path,"wb") as f:
        f.write(voice)

    data,fs = sf.read(file_path)
    sd.play(data,fs)
    sd.wait()

if __name__ == "__main__":
    while True:
        time.sleep(10)
        play_reply(comment="おはようございます",reply="おはようございます！✨ 今日も頑張りましょう！")


```



#### Google cloud

Macの場合

> export YOUTUBE_API_KEY=API

#### Google gemini

Google geminiを利用して、自動会話ができます。

```python
# pip install -q -U google-genai
from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY= os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)


def getReply(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message)
    return response.text

if __name__ == "__main__":
    result= getReply(message="good day")
    print(result)
```

#### YouTube Data API v3

このApiはYouTubeでチャットを行うデータを呼び出す。

```python

import requests
import os
import pprint
import time
import gemini_api
import sound_api
from dotenv import load_dotenv

load_dotenv()

def get_chat_id(api_key, live_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"key": api_key, "part": "liveStreamingDetails", "id": live_id}
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        json = res.json()
        return json["items"][0]["liveStreamingDetails"].get("activeLiveChatId")
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        pprint.pprint(f"チャットID取得エラー: {e}")
        return None

def get_latest_comment(api_key, chat_id, page_token=None):
    url = "https://www.googleapis.com/youtube/v3/liveChat/messages"
    params = {"key": api_key, "part": "snippet", "liveChatId": chat_id, "maxResults": 2}
    if page_token:
        params["pageToken"] = page_token
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        resource = res.json()
        comments = [item["snippet"]["textMessageDetails"]["messageText"] for item in resource.get("items", [])]
        return comments[-1] if comments else None, resource.get("nextPageToken")
    except requests.exceptions.RequestException as e:
        pprint.pprint(f"コメント取得エラー: {e}")
        return None, None

def main():
    api_key = os.getenv('YOUTUBE_API_KEY')
    live_id = "QfUlYtbZPkY"
    chat_id = get_chat_id(api_key, live_id)
    if not chat_id:
        pprint.pprint("チャットIDを取得できませんでした。")
        return
    pprint.pprint(f"チャットID: {chat_id}")
    page_token = None
    while True:
        comment, page_token = get_latest_comment(api_key, chat_id, page_token)
        if comment:
            reply = gemini_api.getReply(comment)
            sound_api.play_reply(comment, reply)
            pprint.pprint(f"新しいコメント: {comment}")
        time.sleep(10)

if __name__ == "__main__":
    main()

```

### まとめ

OBSでYoutubeの生放送できます。

VRoid StudioやMagic Mirror、3teneFREE_betaなどを利用して3Dキャラクターが生成できます。

YouTube Data API v3を利用して、YouTubeでチャットを行うデータを呼び出すことができます。

Google geminiを利用して3Dキャラクターの脚本を生成することができます。

VOICEVOXを利用して、模擬音声を生成する。

OBSで組み合わせてAI数字人を活用したライブコマースができます。

#### 開発のレーソン

https://www.youtube.com/watch?v=WVpvExDPgOE

