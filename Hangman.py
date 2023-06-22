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
