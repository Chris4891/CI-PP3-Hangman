import tkinter as tk
import random
import math

def load_words_from_txt_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words    


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

