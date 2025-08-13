import os 
from dotenv import load_dotenv
from models.gemini import  function_model as gemini_model
from models.open_router import function_model as qwen_model
import argparse

load_dotenv(dotenv_path=".env")

parser = argparse.ArgumentParser("Zia")

parser.add_argument("-q", "--qwen", help="Use a Qwen", action="store_true")
parser.add_argument("-g", "--gemini", help="Use a Gemini", action="store_true")
parser.add_argument("model", type=str, help="model", nargs="?")

args = parser.parse_args()

if args.qwen:
    if args.model:
        qwen_model(qwen_model==args.model, system_prompt=os.getenv("SYSTEM_PROMPT"))
    else:
        qwen_model(system_prompt=os.getenv("SYSTEM_PROMPT"))
elif args.gemini:
    if args.model:
        gemini_model(google_model=args.model, system_prompt=os.getenv("SYSTEM_PROMPT"))
    else:
        gemini_model(system_prompt=os.getenv("SYSTEM_PROMPT"))
else:
    if args.model:
        gemini_model(google_model=args.model, system_prompt=os.getenv("SYSTEM_PROMPT"))
    else:
        gemini_model(system_prompt=os.getenv("SYSTEM_PROMPT"))