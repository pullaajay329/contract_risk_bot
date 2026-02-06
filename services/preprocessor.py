import re
def clean_text(text:str) -> str:
    text = re.sub(r'[^a-zA-Z0-9]',' ',text)
    text = text.replace(" "," ")
    return text