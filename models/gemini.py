import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv(dotenv_path='.env')
def functionModel(googleModel:str="gemini-2.5-flash", systemPrompt:str = "Your name is Lucy"):
    text = input("")
    client = genai.Client(api_key=os.getenv("API_KEY_GOOGLE"))

    response = client.models.generate_content_stream(
        model=googleModel, config=types.GenerateContentConfig(
        system_instruction=systemPrompt) ,contents=text,
    )
    for chunk in response:
        print(chunk.text, end="")

