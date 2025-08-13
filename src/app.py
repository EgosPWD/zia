import os 
from dotenv import load_dotenv
from models.gemini import  function_model as gemini_model
from models.open_router import function_model as qwen_model
from utils.system_promt import load_system_prompt, save_system_prompt
import argparse

load_dotenv(dotenv_path=".env")

parser = argparse.ArgumentParser("Zia")

parser.add_argument("-q", "--qwen", help="use a Qwen", action="store_true")
parser.add_argument("-g", "--gemini", help="use a Gemini", action="store_true")
parser.add_argument("model", type=str, help="model", nargs="?")
parser.add_argument("-sp","--set-prompt", type=str, help="change and save the system prompt")

args = parser.parse_args()

if args.set_prompt:
    save_system_prompt(args.set_prompt)
    system_prompt = args.set_prompt
else:
    system_prompt = load_system_prompt()


if args.qwen:
    if args.model:
        qwen_model(qwen_model==args.model, system_prompt=system_prompt)
    else:
        qwen_model(system_prompt=system_prompt)
elif args.gemini:
    if args.model:
        gemini_model(google_model=args.model, system_prompt=system_prompt)
    else:
        gemini_model(system_prompt=system_prompt)
else:
    if args.model:
        gemini_model(google_model=args.model, system_prompt=system_prompt)
    else:
        gemini_model(system_prompt=system_prompt)