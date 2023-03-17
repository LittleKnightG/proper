import random

SUBJECT_FILES = {
    "math": "math_questions.txt",
    "business studies": "business_questions.txt",
    "computer science": "cs_questions.txt",
    "physics": "physics_questions.txt",
    "chemistry": "chemistry_questions.txt",
    "biology": "biology_questions.txt",
    "economics": "economics_questions.txt",
    "geography": "geography_questions.txt",
    "english lit": "english_lit_questions.txt",
    "religious studies": "religious_studies_questions.txt",
}


def generate_math_questions(num_questions):
    operations = ["add", "subtract", "multiply", "divide"]
    questions = []
    answers = []
    for i in range(num_questions):
        operation = random.choice(operations)
        if operation == "add":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            question = f"What is {a} + {b}?"
            answer = str(a + b)
        elif operation == "subtract":
            a = random.randint(1, 100)
            b = random.randint(1, a)
            question = f"What is {a} - {b}?"
            answer = str(a - b)
        elif operation == "multiply":
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            question = f"What is {a} x {b}?"
            answer = str(a * b)
        elif operation == "divide":
            a = random.randint(1, 144)
            b = random.randint(1, 12)
            question = f"What is {a} / {b}?"
            answer = str(int(a / b))
        questions.append(question)
        answers.append(answer)
    return questions, answers

def read_lines_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def get_subject():
    subjects = list(SUBJECT_FILES.keys())
    while True:
        subject = input(f"Choose a subject ({'/'.join(subjects)}): ")
        if subject in subjects:
            return subject
        else:
            print(f"Error: Invalid subject {subject}")

def get_num_questions():
    while True:
        try:
            num_questions = int(input("How many questions do you want to answer? "))
            if num_questions > 0:
                return num_questions
            else:
                print("Error: Number of questions must be greater than 0")
        except ValueError:
            print("Error: Please enter a valid integer")

def get_name():
    name = input("What is your name? ")
    return name

def get_score(name, subject):
    try:
        with open(f"{name}_{subject}_score.txt", "r") as f:
            score = int(f.read())
    except FileNotFoundError:
        score = 0
    return score

def update_score(name, subject, score):
    with open(f"{name}_{subject}_score.txt", "w") as f:
        f.write(str(score))
        print(15)

def play_game(name, subject, questions, answers, num_questions):
    num_questions = min(num_questions, len(questions))
    print(f"\n{' '.join(questions[0].split()[:2]).capitalize()} Questions:")
    score = 0
    for i in range(num_questions):
        index = random.randrange(len(questions))
        question = questions[index]
        answer = answers[index]
        response = input(f"\nQuestion {i+1}: {question}\n")
        if response.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
    print(f"\n{name}'s score for {subject}: {score}")
    update_score(name, subject, score)


def main():
    name = get_name()
    subject = get_subject()
    num_questions = get_num_questions()
    if subject == "math":
        questions, answers = generate_math_questions(num_questions)
    else:
        filename = SUBJECT_FILES[subject]
        questions = read_lines_from_file(filename)
        answers = read_lines_from_file(filename.replace("questions", "answers"))
    play_game(name, subject, questions, answers, num_questions)
    while True:
        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() == "yes":
            subject = get_subject()
            num_questions = get_num_questions()
            if subject == "math":
                questions, answers = generate_math_questions(num_questions)
            else:
                filename = SUBJECT_FILES[subject]
                questions = read_lines_from_file(filename)
                answers = read_lines_from_file(filename.replace("questions", "answers"))
            play_game(name, subject, questions, answers, num_questions)
        else:
            break


if __name__ == "__main__":
    main()
