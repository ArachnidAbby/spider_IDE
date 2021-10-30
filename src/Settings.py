import json
global EDITOR, Highlighting


with open("src/settings/editor.json") as f:
    EDITOR = json.load(f)
with open(f"{EDITOR['Theme']}/SyntaxColors.json") as f:
    Highlighting = json.load(f)