# Simple Quiz Game (exactly 50 lines)

import random
import time

questions = [
    {"q": "What is the capital of France? duplicate 1, 2, 3, 4", "a": "paris"},
    {"q": "What is 5 + 7?", "a": "12"},
    {"q": "Who wrote 'Romeo and Juliet'?", "a": "shakespeare"},
    {"q": "What planet is known as the Red Planet?", "a": "mars"},
    {"q": "What is the largest mammal?", "a": "blue whale"},
    {"q": "How many continents are there?", "a": "7"},
    {"q": "What gas do plants breathe in?", "a": "carbon dioxide"},
    {"q": "What is H2O commonly known as?", "a": "water"},
    {"q": "What is the fastest land animal?", "a": "cheetah"},
    {"q": "Who painted the Mona Lisa?", "a": "da vinci"}
]

def intro():
    print("==============================")
    print("     🧠 Welcome to QuizMe!    ")
    print("==============================")
    print("You’ll get 5 random questions.")
    print("Type your answers carefully!\n")

def ask_question(q):
    print(q["q"])
    answer = input("Your answer: ").strip().lower()
    if answer == q["a"]:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer was '{q['a']}'.\n")
        return False

def run_quiz():
    score = 0
    selected = random.sample(questions, 5)
    for q in selected:
        if ask_question(q):
            score += 1
        time.sleep(0.5)
    return score

def main():
    intro()
    total_score = run_quiz()
    print("==============================")
    print(f"🎯 You scored {total_score} out of 5!")
    if total_score == 5:
        print("🏆 Perfect! You’re a genius!")
    elif total_score >= 3:
        print("👍 Great job!")
    else:
        print("💪 Keep practicing!")
    print("==============================")

if __name__ == "__main__":
    main()
