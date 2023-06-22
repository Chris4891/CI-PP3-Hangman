import tkinter as tk
import random
import math

def load_words_from_txt_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words    

def start_game():
    username = username_entry.get()

    if username:
        username_label.pack_forget()
        username_entry.pack_forget()
        start_button.pack_forget()

        initialize_game()
        window.title(f"Hangman Game - {username}")

    else:
        message_label.config(text="Please enter your name.")

def initialize_game():
    global guess_word, remaining_attempts, guessed_letters
    guess_word = random.choice(words)
    remaining_attempts = 6
    guessed_letters = set()
    update_word_display()
    update_image()

def update_word_display():
    masked_word = ' '.join([letter if letter in guessed_letters else '_' for letter in guess_word])
    word_label.config(text=masked_word)

def update_image():
    image_path = f'img/hangman{6 - remaining_attempts}.png'
    hangman_image.config(file=image_path)

def process_guess():
    global remaining_attempts

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            message_label.config(text="You've already guessed that letter.")
        elif guess in guess_word:
            guessed_letters.add(guess)
            update_word_display()

            if all(letter in guessed_letters for letter in guess_word):
                message_label.config(text="Congratulations! You guessed the word!")
        else:
            remaining_attempts -= 1
            update_image()

            if remaining_attempts == 0:
                message_label.config(text="game ended")

    else:
        message_label.config(text="Please enter a single letter.")

# GUI
window = tk.Tk()
window.title("Hangman Game")

window.configure(bg="white")

username_label = tk.Label(window, text="Enter your name:", font=('Arial', 18), bg="white")
username_label.pack(pady=20)

username_entry = tk.Entry(window, font=('Arial', 16))
username_entry.pack()

start_button = tk.Button(window, text="Start Game", command=start_game, font=('Arial', 16), bg="white")
start_button.pack(pady=20)

hangman_image = tk.PhotoImage(file="img/hangman0.png")
hangman_label = tk.Label(window, image=hangman_image, bg="white")

word_label = tk.Label(window, font=('Arial', 24), bg="white")
guess_label = tk.Label(window, text="Guess a letter:", font=('Arial', 18), bg="white")
guess_entry = tk.Entry(window, font=('Arial', 24))
guess_button = tk.Button(window, text="Guess", command=process_guess, font=('Arial', 16), bg="white")
message_label = tk.Label(window, font=('Arial', 18), bg="white")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = math.floor(screen_width * 0.8)
window_height = math.floor(screen_height * 0.8)
window_x = math.floor((screen_width - window_width) / 2)
window_y = math.floor((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
