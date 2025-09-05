import os
from openai import OpenAI

key = "xxxxxxxx"

messages = []
client = OpenAI(api_key=key, base_url="https://api.perplexity.ai")






def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )


    response = client.chat.completions.create(messages=messages,
        model="sonar-pro",
    )
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }
    
    messages.append(message)
    print(f"Assistant: {response.choices[0].message.content}")

if __name__ == "__main__":
    user_question = input("Hi I am Your Assistant, How may I help you?\n")
    completion(user_question)

print(messages)






