import pytest
import json
import os
from src.storage import save_results

TEST_FILEPATH = "data/test_history.json"

def teardown_function():
    """Delete test file after each test."""
    if os.path.exists(TEST_FILEPATH):
        os.remove(TEST_FILEPATH)

def test_save_creates_file():
    results = [{"id": "THM_001", "result": True}]
    save_results(results, filepath=TEST_FILEPATH)
    assert os.path.exists(TEST_FILEPATH)

def test_save_correct_content():
    results = [{"id": "THM_001", "result": True}]
    save_results(results, filepath=TEST_FILEPATH)
    with open(TEST_FILEPATH, "r") as f:
        history = json.load(f)
    assert len(history) == 1
    assert history[0]["id"] == "THM_001"
    assert history[0]["result"] == True

def test_save_accumulates():
    results1 = [{"id": "THM_001", "result": True}]
    results2 = [{"id": "ALG_001", "result": False}]
    save_results(results1, filepath=TEST_FILEPATH)
    save_results(results2, filepath=TEST_FILEPATH)
    with open(TEST_FILEPATH, "r") as f:
        history = json.load(f)
    assert len(history) == 2