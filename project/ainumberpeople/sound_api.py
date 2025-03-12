
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

