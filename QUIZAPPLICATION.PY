def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Data Analysis?",
        "options": ["A. HTML", "B. CSS", "C. Python", "D. XML"],
        "answer": "C"
    },
    {
        "question": "What does SQL stand for?",
        "options": [
            "A. Structured Query Language",
            "B. Simple Query Language",
            "C. Standard Question Language",
            "D. None"
        ],
        "answer": "A"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": [
            "A. Alan Turing",
            "B. Charles Babbage",
            "C. Newton",
            "D. Einstein"
        ],
        "answer": "B"
    }
]


def start_quiz():

    score = 0

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        user_answer = input("Enter Answer: ").upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    percentage = (score / len(questions)) * 100

    print("\n===== RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", calculate_grade(percentage))


while True:

    print("\n===== QUIZ APPLICATION =====")
    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")