import pytest
from src.loader import load_questions

SAMPLE_CSV = "data/sample.csv"

def test_load_returns_list():
    questions = load_questions(SAMPLE_CSV)
    assert isinstance(questions, list)

def test_load_not_empty():
    questions = load_questions(SAMPLE_CSV)
    assert len(questions) > 0

def test_questions_have_required_keys():
    questions = load_questions(SAMPLE_CSV)
    required_keys = {"id", "subject", "topic", "question", "answer", "difficulty"}
    for q in questions:
        assert required_keys.issubset(q.keys())

def test_filter_by_subject():
    questions = load_questions(SAMPLE_CSV)
    filtered = [q for q in questions if q["subject"].lower() == "maths 2"]
    assert len(filtered) > 0
    assert all(q["subject"].lower() == "maths 2" for q in filtered)