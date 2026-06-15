import json
import os
from collections import defaultdict
def calculate_priorities(questions, history_filepath="data/history.json"):
    """
    Returns questions sorted by priority score.
    Score = total_fails - total_correct
    Higher score = higher priority (appears first)
    """
     # Load history if exists
    if os.path.exists(history_filepath):
        with open(history_filepath, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Calculate score per question id
    scores = defaultdict(lambda: {"correct": 0, "fails": 0})

    for entry in history:
        if entry["result"]:
            scores[entry["id"]]["correct"] += 1
        else:
            scores[entry["id"]]["fails"] += 1
 # Assign priority score to each question
    def get_score(q):
        s = scores[q["id"]]
        return s["fails"] - s["correct"]

    # Sort questions by score descending (highest priority first)
    return sorted(questions, key=get_score, reverse=True)