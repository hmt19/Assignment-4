import random

score = 0

for i in range(10):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = num1 * num2
    user_answer = int(input(f"What is {num1} x {num2}? "))

    if user_answer == answer:
        print("Right!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {answer}.")

print(f"You got {score} out of 10 questions correct.")
