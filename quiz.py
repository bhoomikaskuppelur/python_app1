import json

# ----------------------------
# Load Questions
# ----------------------------
try:
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
except FileNotFoundError:
    print("Error: questions.json not found!")
    exit()

# ----------------------------
# Quiz Variables
# ----------------------------
score = 0
results = []

print("=" * 60)
print("              TERMINAL QUIZ SYSTEM")
print("=" * 60)

print("\nAnswer using A, B, C or D.\n")

# ----------------------------
# Quiz Starts
# ----------------------------
for index, question in enumerate(questions, start=1):

    print(f"\nQuestion {index}")
    print("-" * 60)
    print(question["question"])
    print()

    option_letters = ["A", "B", "C", "D"]

    for i, option in enumerate(question["options"]):
        print(f"{option_letters[i]}. {option}")

    while True:
        answer = input("\nYour Answer (A/B/C/D): ").strip().upper()

        if answer in option_letters:
            break
        else:
            print("Invalid input! Enter A, B, C or D.")

    selected_option = question["options"][option_letters.index(answer)]
    correct_answer = question["answer"]

    if selected_option == correct_answer:
        score += 1
        result = "Correct"
    else:
        result = "Wrong"

    results.append({
        "question": question["question"],
        "your_answer": selected_option,
        "correct_answer": correct_answer,
        "result": result
    })

# ----------------------------
# Final Report
# ----------------------------
print("\n")
print("=" * 90)
print("                        QUIZ REPORT")
print("=" * 90)

header = f"{'No':<4}{'Your Answer':<35}{'Correct Answer':<35}{'Result'}"
print(header)
print("-" * 90)

for i, item in enumerate(results, start=1):
    print(
        f"{i:<4}"
        f"{item['your_answer']:<35}"
        f"{item['correct_answer']:<35}"
        f"{item['result']}"
    )

print("-" * 90)

wrong = len(questions) - score
percentage = (score / len(questions)) * 100

print(f"\nTotal Questions : {len(questions)}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong}")
print(f"Score           : {percentage:.2f}%")

print("\nPerformance")

if percentage == 100:
    print("⭐⭐⭐⭐⭐ Outstanding!")
elif percentage >= 80:
    print("⭐⭐⭐⭐ Excellent!")
elif percentage >= 60:
    print("⭐⭐⭐ Good Job!")
elif percentage >= 40:
    print("⭐⭐ Keep Practicing!")
else:
    print("⭐ Don't Give Up! Practice More!")

print("\nThank you for playing the quiz!")