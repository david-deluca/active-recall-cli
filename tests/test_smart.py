import pytest
from src.smart import calculate_priorities
from src.loader import load_questions

SAMPLE_CSV = "data/sample.csv"

def test_returns_all_questions():
    questions = load_questions(SAMPLE_CSV)
    result = calculate_priorities(questions)
    assert len(result) == len(questions)

def test_failed_questions_come_first():
    questions = load_questions(SAMPLE_CSV)
    # Simulate history where first question was failed 3 times
    import json, os
    test_history = [
        {"id": questions[0]["id"], "result": False},
        {"id": questions[0]["id"], "result": False},
        {"id": questions[0]["id"], "result": False},
    ]
    test_filepath = "data/test_smart_history.json"
    with open(test_filepath, "w") as f:
        json.dump(test_history, f)

    result = calculate_priorities(questions, history_filepath=test_filepath)
    assert result[0]["id"] == questions[0]["id"]

    os.remove(test_filepath)