import json
import os

FILENAME = "dist/library.json"

def load_library():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_library(library):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)
