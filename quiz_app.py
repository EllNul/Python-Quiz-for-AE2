from quiz_engine import QuizEngine

engine = QuizEngine()

while True:
    q = engine.current_question()

    print("\nQUESTION:", q["question"])
    for i, option in enumerate(q["options"]):
        print(f"{i}. {option}")

    choice = int(input("Your answer: "))

    is_correct = engine.check_answer(choice)
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect!")
        print("Correct answer:", engine.correct_answer_text())

    if not engine.next_question():
        break

print("\nQUIZ COMPLETE!")
print("Your score:", engine.score)