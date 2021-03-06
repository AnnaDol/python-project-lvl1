#!/usr/bin/env python
import prompt
from random import randint


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello():
    print("Welcome to the Brain Games!")


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))


def even_or_not(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')
    q = 0
    counter = 3
    while counter > 0:
        number = randint(1, 1000)
        print('Question: {}'.format(number))
        text = input("Answer: ")
        if (number % 2 == 0 and text == 'yes') \
           or (number % 2 != 0 and text == 'no'):
            print("Correct!")
            q += 1
        else:
            print("Answer is wrong ;(. \nLet's try again, {}!".format(name))
            return
        counter -= 1
    winner_or_loser(q, name)


def main():
    hello()
    name = prompt.string('May I have your name? ')
    welcome_user(name)
    even_or_not(name)


if __name__ == "__main__":
    main()
