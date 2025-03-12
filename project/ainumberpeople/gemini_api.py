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