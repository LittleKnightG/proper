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
        with open(f"{subject}_scores.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line_parts = line.strip().split()
                if line_parts[0] == name:
                    score = int(line_parts[1])
                    return score
            # If the name wasn't found in the file, assume score is 0
            score = 0
    except FileNotFoundError:
        score = 0
    return score


def update_score(name, subject, score):
    with open(f"{subject}_scores.txt", "a") as f:
        f.write(f"{name} {score}\n")

def play_game(name, subject, questions, answers, num_questions):
    num_questions = min(num_questions, len(questions)) # Ensure that the number of questions asked is not more than the number of available questions
    print(f"Welcome {name}! Let's play {subject} quiz with {num_questions} questions.")
    score = 0
    for i in range(num_questions):
        question = random.choice(questions)
        correct_answer = answers[questions.index(question)]
        user_answer = input(question + " ")
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}")
    print(f"Game over! You scored {score} out of {num_questions}")
    update_score(name, subject, score)

def main():
    name = get_name()
    subject = get_subject()
    num_questions = get_num_questions()
    if subject.lower() == "math":
        questions, answers = generate_math_questions(num_questions)
    else:
        filename = SUBJECT_FILES[subject.lower()]
        questions = read_lines_from_file(filename)
        answers = [line.split(",")[1] for line in questions]
        questions = [line.split(",")[0] for line in questions]
    play_game(name, subject, questions, answers, num_questions)

if __name__ == "__main__":
    main()
