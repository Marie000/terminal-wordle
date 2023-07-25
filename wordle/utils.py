import json

with open('./texts.json', 'r') as f:
  text_data = json.load(f)

def get_text(name, language, variables=[]):
    return text_data[name][language].format(*variables)
