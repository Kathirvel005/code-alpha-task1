import random

# List of predefined words
words = ["python", "apple", "ocean", "robot", "planet"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect attempts.\n")

while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!\n")
    else:
        incorrect_guesses += 1
        remaining = max_attempts - incorrect_guesses
        print(f"❌ Wrong! Attempts left: {remaining}\n")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
