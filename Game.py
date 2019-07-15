import random, sys
from typing import List

WORD_LIST = [
"python", "umbrella", "window", "computer", "javascript", "supreme", "macbook", "desktop",
 "windows", "opportunity", "tmobile","Starbucks", "feedback", "Samsung","adidas", "ultra boost", "raiders","nike"
           ]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) 
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_word_to_guess(letters: List) -> None:
    print("Word to guess: {0}".format(" ".join(letters)))

def print_guesses_taken(current: int, total: int) -> None:
    print("You are on guess {0}/{1}.".format(current, total))

def beginning() -> None:
    print("Yoo whats up!!\n")
    while True:
        name = input("What is your name\n").strip()
        if name == '':
            print("Nah can't do that! No blank lines")
        else:
            break

def ask_user_to_play() -> None:
    print("Well, Lets play some Hangman!!!!!\n")
    while True:
        gameChoice = input("Would You like to play ?\n").upper()
        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("Oh no, well thats a bummer. Have a chill day")
        else:
            print("YO, Answer only Yes or No.")
            continue

def prepare_secret_word() -> None:
    for character in SECRET_WORD:
        GUESS_WORD.append("-")
    print("Ok, Time to guess the word", LENGTH_WORD, "characters")
    print("Enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)

def guessing() -> None:
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess in ALPHABET: 
            print("Enter a letter from a-z ALPHABET")
        elif guess in letter_storage: 
            print("Yikes you guessed that letter!")
        else: 
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("Yee!! You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("Oh,try a different letter!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" Yikes, YOU LOST :(! The secret word was {0}".format(SECRET_WORD))

if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()