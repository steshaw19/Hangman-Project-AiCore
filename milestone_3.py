## Imports random generator function
import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]

## Generates a random word from word_list
word = random.choice(word_list)

## Converts the guess to lowercase and checks if it is in the word
def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

## Takes user input and checks if it is a single letter and is alphabetical.
def ask_for_input():
    guess = input("Please choose a letter: ")
    while True:
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            break
        else:
            print("This is a valid guess.")
            check_guess(guess)
            break
    

ask_for_input()
    
   