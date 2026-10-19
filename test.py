import random

words = ["python", "computer", "college", "program", "coding"]

word = random.choice(words)
guessed = []
wrong = 0

print("===== HANGMAN GAME =====")

while wrong < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong += 1
        print("Wrong guess!")
        print("Wrong attempts:", wrong, "/ 6")

else:
    print("\n💀 You Lose!")
    print("Correct word was:", word)
    