#!/usr/bin/env python
import prompt
from random import randint, choice
from operator import add, mul, sub


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello():
    print("Welcome to the Brain Games!")


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))


def calculate_numbers(name):
    q = 0
    counter = 3
    print('What is the result of the expression?')
    while counter > 0:
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        operators = ('+', '-', '*')
        operator = choice(operators)
        print('Question: {} {} {}'.format(number_one, operator, number_two))
        text = input("Answer: ")
        if (operator == '+' and text == str(add(number_one, number_two))) \
            or (operator == '-' and text == str(sub(number_one, number_two))) \
                or (operator == '*' and text == str
                    (mul(number_one, number_two))):
            print("Correct!")
            q += 1
        elif operator == '+' and text != str(add(number_one, number_two)):
            print(
                "{} is wrong answer ;(. Correct answer was {}. "
                "\nLet's try again, {}!".format(text,
                                                str(add(number_one,
                                                        number_two)), name))
            return
        elif operator == '-' and text != str(sub(number_one, number_two)):
            print(
                "{} is wrong answer ;(. Correct answer was {}. "
                "\nLet's try again, {}!".format(text,
                                                str(sub(number_one,
                                                        number_two)), name))
            return
        else:
            print(
                "{} is wrong answer ;(. Correct answer was {}. "
                "\nLet's try again, {}!".format(text,
                                                str(mul(number_one,
                                                        number_two)), name))
            return
        counter -= 1
    winner_or_loser(q, name)


def main():
    hello()
    name = prompt.string('May I have your name? ')
    welcome_user(name)
    calculate_numbers(name)


if __name__ == "__main__":
    main()
