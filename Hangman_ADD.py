import tkinter as tk
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

# Initialize main game variables
word = random.choice(words)
guessed_word = ["_" for _ in word]
guessed_letters = []
attempts = 6

# Create the main application window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x550")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#ff5733")
title_label.pack(pady=20)

# Labels for displaying the hangman image and the word status
hangman_label = tk.Label(root, text=hangman_stages[0], font=("Courier", 16), bg="#f0f8ff", fg="#555555")
hangman_label.pack(pady=10)

word_label = tk.Label(root, text=" ".join(guessed_word), font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333333")
word_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#ff3333")
result_label.pack(pady=10)


# Function to handle letter button clicks
def guess_letter(letter):
    global attempts
    if letter in guessed_letters:
        return  # Skip if already guessed

    guessed_letters.append(letter)
    if letter in word:
        # Reveal the letter in the word
        for i, l in enumerate(word):
            if l == letter:
                guessed_word[i] = letter
        word_label.config(text=" ".join(guessed_word))

        # Check for win
        if "_" not in guessed_word:
            result_label.config(text="Congratulations! You've won!", fg="#4CAF50")
            disable_buttons()
    else:
        # Incorrect guess
        attempts -= 1
        hangman_label.config(text=hangman_stages[6 - attempts])
        if attempts == 0:
            result_label.config(text=f"Game Over! The word was '{word}'", fg="#ff3333")
            disable_buttons()


# Function to disable all buttons
def disable_buttons():
    for button in letter_buttons:
        button.config(state=tk.DISABLED)


# Hover effect for buttons
def on_enter(button):
    button.config(bg="#87CEFA", fg="#ffffff")


def on_leave(button):
    button.config(bg="#add8e6", fg="#000000")


# Create letter buttons
letter_buttons = []
letters_frame = tk.Frame(root, bg="#f0f8ff")
letters_frame.pack(pady=20)

for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    button = tk.Button(
        letters_frame,
        text=letter.upper(),
        width=4,
        height=2,
        font=("Helvetica", 14, "bold"),
        command=lambda l=letter: guess_letter(l),
        bg="#add8e6",
        fg="#000000",
        activebackground="#87CEFA",
        activeforeground="#ffffff",
        relief="raised",
        borderwidth=2
    )

    button.grid(row=i // 9, column=i % 9, padx=5, pady=5)

    button.bind("<Enter>", lambda e, b=button: on_enter(b))
    button.bind("<Leave>", lambda e, b=button: on_leave(b))

    letter_buttons.append(button)

# Start the game
root.mainloop()
