import openai
import pprint
import os
from dotenv import load_dotenv


load_dotenv()
# 自分のAPIキーをセット
api_key = os.getenv('OPEN_API_KEY')
client = openai.Client(api_key=api_key)
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # ユーザーとのチャット
    pprint.pprint("Chatbot: こんにちは！質問があればどうぞ。")  

    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() == "exit":
    #         ("Chatbot: さようなら！")
    #         break
    #     response = chat_with_gpt(user_input)
    #     pprint.pprint(f"Chatbot: {response}")

    response = chat_with_gpt("good day")
    pprint.pprint(f"Chatbot: {response}")