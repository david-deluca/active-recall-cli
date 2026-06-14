import json
import os
from datetime import datetime
def save_results(results, filepath="data/history.json"):
    """
    Appends session results to the history JSON file.
    Each result is a dict with keys: id, result, timestamp.
    """
     # Load existing history if file exists
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Add timestamp to each result
    for r in results:
        r["timestamp"] = datetime.now().isoformat()

    # Append new results
    history.extend(results)

    # Save back to file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)