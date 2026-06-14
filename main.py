import random
from storage import save_results
from loader import load_questions

def run_session(filepath, n=5):
    """
    Runs a study session with n questions loaded from filepath.
    """
    questions = load_questions(filepath)
    selected = random.sample(questions, min(n, len(questions)))
    
    correct = 0
    total = len(selected)
    results = []

    for q in selected:
        print("\n" + "="*40)
        print(f"Subject: {q['subject']} | Topic: {q['topic']}")
        print(f"\nQ: {q['question']}")
        
        input("\nPress Enter to see the answer...")
        
        print(f"\nA: {q['answer']}")
        
        response = input("\nDid you get it right? (y/n): ").strip().lower()
        results.append({
            "id": q["id"],
            "result": response == "y"
        })
        if response == 'y':
            correct += 1

    print("\n" + "="*40)
    print(f"Session complete: {correct}/{total} correct ({round(correct/total*100)}%)")

    save_results(results)
    print("Results saved to data/history.json")

if __name__ == "__main__":
    run_session("data/sample.csv", n=5)