## Imports random generator function
import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):

        # attributes
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guessed = []

    def check_guess(self, guess):
        guess_lower = guess.lower()
        if guess_lower in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess_lower:
                    self.word_guessed[index] = guess
                    print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    ## Takes user input and checks if it is a single letter and is alphabetical.
    def ask_for_input(self):
        guess = input("Please choose a letter: ")
        while True:
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif guess in self.list_of_guessed:
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guessed.append(guess)
                break
    
  
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while game.num_lives > 0:
        play_again = game.ask_for_input()
        if game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
    else:
        print("You lost!")

play_game(word_list)
