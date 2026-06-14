import random
import argparse
from storage import save_results
from loader import load_questions

def run_session(filepath, n=5, subject=None, difficulty=None):
    """
    Runs a study session with n questions loaded from filepath.
    """
    questions = load_questions(filepath)
    if subject:
        questions = [q for q in questions if q['subject'].lower() == subject.lower()]
    
    if difficulty:
        questions = [q for q in questions if int(q['difficulty']) >= difficulty]
    
    if not questions:
        print("No questions found with those filters.")
        return
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
    parser = argparse.ArgumentParser(description="Active Recall CLI Tool")
    parser.add_argument("--subject", type=str, default=None, help="Filter by subject")
    parser.add_argument("--difficulty", type=int, default=None, help="Minimum difficulty level")
    parser.add_argument("--n", type=int, default=5, help="Number of questions per session")
    args = parser.parse_args()

    run_session("data/sample.csv", n=args.n, subject=args.subject, difficulty=args.difficulty)