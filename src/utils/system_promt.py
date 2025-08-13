import os
PROMPT_FILE = "src/config/system_prompt.txt"
def load_system_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()
def save_system_prompt(new_prompt):
    with open(PROMPT_FILE,"w", encoding="utf-8") as f:
        f.write(new_prompt.strip())


