import random
import colorama
from colorama import Fore, Style

colorama.init()

def load_words_from_txt_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words




def initialize_game(words):
    global guess_word, remaining_attempts, guessed_letters
    guess_word = random.choice(words)
    remaining_attempts = 6
    guessed_letters = set()

