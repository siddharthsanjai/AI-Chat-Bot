# AI-Chat-Bot
import os
from openai import OpenAI

key = os.getenv("OPENAI_API_KEY")

messages = []

client = OpenAI(
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create(messages=messages,
        model="gpt-4o",
    )
    print(chat_completion)
    

if __name__ == "__main__":
    user_question = input("Hi I am BAWA, How may I help you?")
    completion(user_question)
