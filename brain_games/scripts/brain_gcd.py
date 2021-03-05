#!/usr/bin/env python
import prompt
from brain_games.games import gcd


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello():
    print("Welcome to the Brain Games!")


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))
    else:
        return print("You lost, {}!".format(name))


def main():
    hello()
    name = prompt.string('May I have your name? ')
    welcome_user(name)
    gcd.find_gcd(name)


if __name__ == "__main__":
    main()
