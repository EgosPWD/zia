import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=".env")

def function_model(qwen_model:str ="qwen/qwen3-30b-a3b:free", system_prompt:str= "Your name is lucy" ):
  text = input("")
  client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=os.getenv("API_KEY_APIROUTER"),
      )

  completion = client.chat.completions.create(

    model=qwen_model,
    messages=[
     {
            "role": "system",
            "content": system_prompt
      },
      {
        "role": "user",
        "content": text
      }
    ], stream=True
  )
  for chunk in completion:
      print(chunk.choices[0].delta.content, end="")

