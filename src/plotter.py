import json
import os
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_progress(history_filepath="data/history.json", output_filepath="output/progress.png"):
    """
    Generates a bar chart of accuracy per subject from history.json
    """
    if not os.path.exists(history_filepath):
        print("No history found. Run a session first.")
        return

    with open(history_filepath, "r", encoding="utf-8") as f:
        history = json.load(f)

    from src.loader import load_questions
    questions = load_questions("data/sample.csv")
    id_to_subject = {q["id"]: q["subject"] for q in questions}

    stats = defaultdict(lambda: {"total": 0, "correct": 0})
    for entry in history:
        subject = id_to_subject.get(entry["id"], "Unknown")
        stats[subject]["total"] += 1
        if entry["result"]:
            stats[subject]["correct"] += 1

    subjects = list(stats.keys())
    accuracies = [round(stats[s]["correct"] / stats[s]["total"] * 100, 1) for s in subjects]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(subjects, accuracies, color="steelblue", edgecolor="black")
    plt.ylim(0, 110)
    plt.ylabel("Accuracy (%)")
    plt.title("Active Recall — Accuracy by Subject")
    plt.axhline(y=80, color="red", linestyle="--", label="Target (80%)")
    plt.legend()

    for bar, acc in zip(bars, accuracies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f"{acc}%", ha="center", fontsize=10)

    plt.tight_layout()
    plt.savefig(output_filepath)
    print(f"Chart saved to {output_filepath}")