import json
from datetime import datetime

def log_audit(data, filename="audit_log.json"):
    data["timestamp"] = str(datetime.now())
    with open(filename, "a") as f:
        json.dump(data, f)
        f.write("\n")