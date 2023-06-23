import os
import random
import colorama
from colorama import Fore, Style


colorama.init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words_from_txt_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words

def start_game():
    clear_screen()
    print(Fore.MAGENTA + "-------------------------------------------")
    print("|                                         |")
    print("|              Hangman Game               |")
    print("|                                         |")
    print(" -------------------------------------------" + Style.RESET_ALL)
    print()

    username = input(Fore.CYAN + "Enter your name: " + Style.RESET_ALL)
    if username:
        print(f"\n{Fore.GREEN}Welcome, {username}! Let's start the game." + Style.RESET_ALL)
        words = load_words_from_txt_file()
        initialize_game(words)
        play_game()
    else:
        print("\nPlease enter your name.")

def initialize_game(words):
    global guess_word, remaining_attempts, guessed_letters
    guess_word = random.choice(words)
    remaining_attempts = 6
    guessed_letters = set()

def update_word_display():
    masked_word = ' '.join(
        [letter if letter in guessed_letters else '_' for letter in guess_word])
    print("Word:", Fore.YELLOW + masked_word + Style.RESET_ALL)


def process_guess():
    global remaining_attempts

    guess = input("Guess a letter: ").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print(Fore.RED + "You've already guessed that letter." + Style.RESET_ALL)
        elif guess in guess_word:
            guessed_letters.add(guess)
            update_word_display()

            if all(letter in guessed_letters for letter in guess_word):
                print(Fore.GREEN + "Congratulations! You guessed the word!" + Style.RESET_ALL)
                end_game()
        else:
            remaining_attempts -= 1

            if remaining_attempts == 0:
                print(Fore.RED + "You ran out of attempts. Game over!" + Style.RESET_ALL)
                print(f"The word was: {guess_word}")
                end_game()
            else:
                print(Fore.RED + "Incorrect guess. Try again." + Style.RESET_ALL)
                print(f"Remaining attempts: {remaining_attempts}")
                display_hangman()
    else:
        print(Fore.RED + "Please enter a single letter." + Style.RESET_ALL)


def display_hangman():
    stages = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
        """, """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
        """, """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
        """, """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
        """, """
            --------
            |      |
            |      O
            |      |
            |      |
            |
        """, """
            --------
            |      |
            |      O
            |
            |
            |
        """, """
            --------
            |      |
            |
            |
            |
            |
        """
    ]
    print("\n" + stages[remaining_attempts - 1] + "\n")


def play_game():
    print(Fore.GREEN + "Let's play Hangman!" + Style.RESET_ALL)
    update_word_display()

    while True:
        process_guess()


def end_game():
    restart = input(Fore.CYAN + "Do you want to play again? (yes/no): " + Style.RESET_ALL)

    if restart.lower() == 'yes':
        initialize_game(words)  
        play_game()
    else:
        print(Fore.YELLOW + "Thank you for playing Hangman!" + Style.RESET_ALL)



words = load_words_from_txt_file()

print(Fore.MAGENTA + "Hangman Game" + Style.RESET_ALL)

start_game()
