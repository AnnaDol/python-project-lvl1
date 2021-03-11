from random import randint


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello():
    print("Welcome to the Brain Games!")


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))
    else:
        return print("You lost, {}!".format(name))


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
            print("Answer is wrong ;(. Let's try again, {}!".format(name))
        counter -= 1
    winner_or_loser(q, name)
