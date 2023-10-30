## Imports random generator function
import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        """ 
        This function initialises the Hangman game class
        
        The function creates the attributes word, word_guessed (i.e. what part of the word has been
        guessed), number of letters in the word, number of lives remaining, a word list variable, and
        generates a list of letters previously guessed by the user.
        """

        # attributes
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guessed = []

    def check_guess(self, guess):
        """
        This function checks if the guess is in the word.
        
        First the function convert any guess into lowercase so that it can be compared with the original word.
        It then checks if this letter is in the word. After, it loops through the word created an indexed list of
        letters - i.e. 0 (a), 1 (p) etc... using the enumerate function. It matches up the guessed letter with the
        index of where it is in the word and replaces a blank space in the self.word_guessed variable in the correct
        place. It will then reduce the number of letters by 1. If the guess is not in the word, the function will
        reduce the lives by one and print the number of lives remaining.
        """
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
        """
        This function takes a user input and checks if it is a valid alphabetical, one-character entry.
        If it is valid it then calls the check_guess function which is checks if the letter is in the word
        and edits the scores appropriately.
        """
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
    """
    This function brings everything together so that the game of Hangman can be played.
    
    It assigns the number of lives and calls the Hangman class. A while loop is then used to play through
    the game until the lives equal to zero (and the player loses), or the number of letters remaining
    equals to zero (the player wins). It breaks out of the loop when the number of lives or number of letters 
    equal zero.
    """
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
