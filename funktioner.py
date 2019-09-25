import random


def random_word(word_list):
    x = random.sample(word_list, 1)
    # source: https://docs.python.org/2/library/random.html
    return x


def guess_input():
    # user_guess = input("Gissa vilket ord det är: ")
    user_guess = "enorm"
    return user_guess
