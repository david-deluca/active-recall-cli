import json
import os
from collections import defaultdict
def show_stats(history_filepath="data/history.json"):
    """
    Reads history.json and prints accuracy statistics per subject.
    """
    if not os.path.exists(history_filepath):
        print("No history found. Run a session first.")
        return
    with open(history_filepath, "r", encoding="utf-8") as f:
        history = json.load(f)

    if not history:
        print("History is empty.")
        return
     
     # We need subject info — load questions to match id -> subject
    from loader import load_questions
    questions = load_questions("data/sample.csv")
    id_to_subject = {q["id"]: q["subject"] for q in questions}
    # Count results per subject
    stats = defaultdict(lambda: {"total": 0, "correct": 0})

    for entry in history:
        subject = id_to_subject.get(entry["id"], "Unknown")
        stats[subject]["total"] += 1
        if entry["result"]:
            stats[subject]["correct"] += 1

    # Print table
    print("\n" + "="*40)
    print("STUDY STATISTICS")
    print("="*40)
    print(f"{'Subject':<20} | {'Total':^5} | {'Correct':^7} | {'Accuracy':^8}")
    print("-"*40)

    for subject, data in stats.items():
        accuracy = round(data["correct"] / data["total"] * 100, 1)
        print(f"{subject:<20} | {data['total']:^5} | {data['correct']:^7} | {accuracy:^7}%")

    print("="*40)