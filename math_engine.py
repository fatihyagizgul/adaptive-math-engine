import random

def generate_question(level):
    if level == "easy":
        max_number = 10
        operations = ["+", "-"]
    elif level == "medium":
        max_number = 50
        operations = ["+", "-", "*"]
    elif level == "hard":
        max_number = 100
        operations = ["+", "-", "*", "/"]
    else:
        raise ValueError("Invalid level")

    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    operation = random.choice(operations)

    question = f"{a} {operation} {b}"

    if operation == "+":
        answer = a + b
    elif operation == "-":
        answer = a - b
    elif operation == "*":
        answer = a * b
    elif operation == "/":
        answer = round(a / b, 2)

    return question, answer


def main():

    levels = ["easy", "medium", "hard"]
    current_level_index = 1  # medium

    total_questions = 5
    correct_count = 0
    start_level = levels[current_level_index]

    correct_streak = 0
    wrong_streak = 0

    for i in range(5):
        level = levels[current_level_index]
        q, correct_answer = generate_question(level)

        print(f"\nQuestion {i+1} (Level: {level})")
        print("Question:", q)

        user_answer = input("Your answer: ")

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input.")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
            correct_streak += 1
            wrong_streak = 0
        else:
            print("Wrong.")
            print("Correct answer was:", correct_answer)
            wrong_streak += 1
            correct_streak = 0

        if correct_streak >= 2 and current_level_index < 2:
            current_level_index += 1
            correct_streak = 0
            print("⬆ Level increased!")

        elif wrong_streak >= 2 and current_level_index > 0:
            current_level_index -= 1
            wrong_streak = 0
            print("⬇ Level decreased!")

    end_level = levels[current_level_index]

    print("\n--- SESSION REPORT ---")
    print("Total questions:", total_questions)
    print("Correct answers:", correct_count)
    print("Wrong answers:", total_questions - correct_count)
    print("Success rate:", round((correct_count / total_questions) * 100, 2), "%")
    print("Start level:", start_level)
    print("End level:", end_level)
if __name__ == "__main__":
    main()
