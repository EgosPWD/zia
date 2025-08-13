import os 
from dotenv import load_dotenv
from models.gemini import functionModel as geminiModel
from models.openRouter import functionModel as qwenModel
import argparse

load_dotenv(dotenv_path=".env")

parser = argparse.ArgumentParser("Zia")

parser.add_argument("-q", "--qwen", help="Use a Qwen", action="store_true")
parser.add_argument("-g", "--gemini", help="Use a Gemini", action="store_true")
parser.add_argument("model", type=str, help="model", nargs="?")

args = parser.parse_args()

if args.qwen:
    if args.model:
        qwenModel(qwenModel=args.model, systemPrompt=os.getenv("SYSTEM_PROMPT"))
    else:
        qwenModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))
elif args.gemini:
    if args.model:
        geminiModel(googleModel=args.model, systemPrompt=os.getenv("SYSTEM_PROMPT"))
    else:
        geminiModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))
else:
    if args.model:
        geminiModel(googleModel=args.model, systemPrompt=os.getenv("SYSTEM_PROMPT"))
    else:
        geminiModel(systemPrompt=os.getenv("SYSTEM_PROMPT"))