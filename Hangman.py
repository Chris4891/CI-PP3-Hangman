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

def update_word_display():
    masked_word = ' '.join(
        [letter if letter in guessed_letters else '_' for letter in guess_word])
    print("Word:", Fore.YELLOW + masked_word + Style.RESET_ALL)