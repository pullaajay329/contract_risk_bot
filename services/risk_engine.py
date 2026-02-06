RISK_RULES = {
    "termination": {
        "keywords": ["terminate", "termination"],
        "risk": "High",
        "reason": "Unilateral termination can harm the business"
    },
    "penalty": {
        "keywords": ["penalty", "liquidated damages"],
        "risk": "High",
        "reason": "Excessive penalties increase financial risk"
    },
    "jurisdiction": {
        "keywords": ["jurisdiction", "governing law"],
        "risk": "Medium",
        "reason": "Foreign jurisdiction increases legal complexity"
    }
}

def assess_clause_risk(clause: str):
    for rule in RISK_RULES.values():
        if any(keyword in clause.lower() for keyword in rule["keywords"]):
            return rule["risk"], rule["reason"]
    return "Low", "No significant risk detected"