import random

# List of words to choose from
words = ["python", "java", "hangman", "computer", "programming", "development", "terminal"]

# Hangman stages for visual representation
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
     --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
     --------
    """
]

# Function to play the Hangman game
def play_hangman():
    word = random.choice(words)  # Randomly select a word
    guessed_letters = []  # Store guessed letters
    attempts = 6  # Number of allowed attempts
    guessed_word = ["_" for _ in word]  # Placeholder for the word with blanks

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
            # Reveal guessed letters in the word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(hangman_stages[6 - attempts])
            print(f"Incorrect! You have {attempts} attempts remaining.")

        # Display the current state of the guessed word
        print(" ".join(guessed_word))

        # Check if the player has guessed the entire word
        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(hangman_stages[6])
        print(f"Game over! The word was '{word}'.")

# Start the game
play_hangman()
