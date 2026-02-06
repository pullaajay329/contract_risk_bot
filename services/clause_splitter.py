import re

def split_into_clauses(text: str):
    clauses = re.split(r'\b\d+\.\s', text)
    return [c.strip() for c in clauses if len(c.strip()) > 20]