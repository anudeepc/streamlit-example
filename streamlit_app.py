import random

def generate_question():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    return num1, num2

def main():
    correct_answers = 0
    total_questions = 10  # You can change this to have more or fewer questions

    for i in range(total_questions):
        num1, num2 = generate_question()
        print(f"Question {i + 1}: What is {num1} * {num2}?")
        
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_answer == num1 * num2:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is {num1 * num2}.")

    print(f"You got {correct_answers} out of {total_questions} questions correct.")

if __name__ == "__main__":
    main()
