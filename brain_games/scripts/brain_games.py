#!/usr/bin/env python
import prompt


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello():
    print("Welcome to the Brain Games!")


def main():
    hello()
    name = prompt.string('May I have your name? ')
    welcome_user(name)


if __name__ == "__main__":
    main()
