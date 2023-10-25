import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]
word = random.choice(word_list)

guess = input("Please choose a letter: ")
while guess.isalpha() == False or len(guess) != 1:
    print("Oops! That is not a valid input.")
    guess = input("Please choose a letter: ")
else:
    print("Good guess!")
