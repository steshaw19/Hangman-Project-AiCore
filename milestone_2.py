import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]
word = random.choice(word_list)


while True:
    guess = input("Please choose a letter: ")
    if guess.isalpha() == False or len(guess) != 1:
        print("Oops! That is not a valid input.")
    else:
        print("Good guess!")
        break
