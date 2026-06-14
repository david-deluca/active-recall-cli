import csv 

def load_questions(filepath):
    """
    Reads a CSV file and returns a list of question dictionaries.
    Each dictionary has keys: id, subject, topic, question, answer, difficulty
    """
    questions = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(row)
    
    return questions