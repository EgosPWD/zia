import os 
from dotenv import load_dotenv
from models.gemini import functionModel as geminiModel
from models.openRouter import functionModel as qwenModel
import argparse

load_dotenv(dotenv_path=".env")

parser = argparse.ArgumentParser("dx")

parser.add_argument("-q", "--qwen", help="Use a Qwen", action="store_true")
parser.add_argument("-g", "--gemini", help="Use a Gemini", action="store_true")

args = parser.parse_args()

if args.qwen:
    qwenModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))
elif args.gemini:
    geminiModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))
    
else:
    # Default Model
    geminiModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))