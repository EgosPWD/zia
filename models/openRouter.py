import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=".env")

def functionModel(qwenModel:str ="qwen/qwen3-30b-a3b:free", systemPrompt:str= "Your name is lucy" ):
  text = input("")
  client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=os.getenv("API_KEY_APIROUTER"),
      )

  completion = client.chat.completions.create(

    model=qwenModel,
    messages=[
     {
            "role": "system",
            "content": systemPrompt
      },
      {
        "role": "user",
        "content": text
      }
    ], stream=True
  )
  for chunk in completion:
      print(chunk.choices[0].delta.content, end="")

