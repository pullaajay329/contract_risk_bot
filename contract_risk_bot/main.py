import os
from services.text_extractor import extract_text
from services.preprocessor import clean_text
from services.clause_splitter import split_into_clauses
from services.risk_engine import assess_clause_risk
from services.llm_service import explain_clause, suggest_alternative
from utils.audit_logger import log_audit


def run_pipeline(file_path):
    raw_text = extract_text(file_path)
    text = clean_text(raw_text)
    clauses = split_into_clauses(text)

    results = []

    for clause in clauses:
        risk, reason = assess_clause_risk(clause)
        explanation = explain_clause(clause)
        suggestion = suggest_alternative(clause)

        results.append({
            "clause": clause,
            "risk": risk,
            "reason": reason,
            "explanation": explanation,
            "suggestion": suggestion
        })

    log_audit({"analysis": results})
    return results


# ✅ WRITE PATH CODE ONLY HERE
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sample_contract.txt")

    print("Looking for file at:", DATA_PATH)
    print("File exists:", os.path.exists(DATA_PATH))

    output = run_pipeline(DATA_PATH)

    for o in output:
        print(o["risk"], o["reason"])