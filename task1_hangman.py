import random

words = ["python", "computer", "program", "network", "student"]
word = random.choice(words)
guessed = []
attempts = 6

print("=== Hangman Game ===")

while attempts > 0:
    display = "".join([ch if ch in guessed else "_" for ch in word])
    print("\nWord:", " ".join(display))

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The word was:", word)