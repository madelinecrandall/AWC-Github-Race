import random

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = input("Your answer (number): ")
    if answer.isdigit() and int(answer) == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f" Incorrect. The correct answer was: {options[correct_answer - 1]}\n")
        return 0

def main():
    print("Welcome to the Git Knowledge Quiz!\n")
    #TODO Make 2 unique Git Questions (1 is done as an example)
    questions = [
        ("What command initializes a new Git repository?", ["git start", "git init", "git new", "git create"], 2),

    ]
    
    random.shuffle(questions)
    score = 0
    
    for question, options, correct_answer in questions:
        score += ask_question(question, options, correct_answer)
    
    print(f"Quiz complete! Your final score: {score}/{len(questions)}")
    

if __name__ == "__main__":
    main()