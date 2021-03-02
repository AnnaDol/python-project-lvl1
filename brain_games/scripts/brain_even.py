import prompt
from random import randint


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello(who):
    print("Welcome to the {}!".format(who))


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))
    else:
        return print("You lost, {}!".format(name))


def even_or_not(name):
    q = 0
    counter = 3
    while counter > 0:
        print('Answer "yes" if the number is even, otherwise answer "no"')
        number = randint(1, 1000)
        print('Question: {}'.format(number))
        text = input("Answer: ")
        if number % 2 == 0 and text == 'yes':
            print("Correct!")
            q += 1
        elif number % 2 != 0 and text == 'yes':
            print(
                "'yes' is wrong answer ;(. Correct answer was 'no'. "
                "\nLet's try again, {}!".format(name))
        elif number % 2 == 0 and text == 'no':
            print(
                "'no' is wrong answer ;(. Correct answer was 'yes'."
                "\nLet's try again, {}!".format(name))
        elif number % 2 != 0 and text == 'no':
            print("Correct!")
            q += 1
        else:
            return print(
                "Answer is wrong ;(. Let's try again,"
                "{}!".format(name))
        counter -= 1

    winner_or_loser(q, name)


def main():
    hello('Brain Games')
    name = prompt.string('May I have your name? ')
    welcome_user(name)
    even_or_not(name)


if __name__ == "__main__":
    main()
