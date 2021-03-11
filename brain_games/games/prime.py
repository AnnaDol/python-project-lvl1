import prompt
from random import randint
name = prompt.string('May I have your name? ')


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))
    else:
        return print("You lost, {}".format(name))


def prime_or_not(name):
    q = 0
    counter = 3
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter > 0:
        number = randint(1, 100)
        print('Question: {}'.format(number))
        text = input("Answer: ")
        x = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                x += 1
        if(x <= 0 and text == 'yes') or (x > 0 and text == 'no'):
            print('Correct!')
            q += 1
        else:
            print("Answer is wrong ;(. Let's try again, {}!".format(name))
        counter -= 1
    winner_or_loser(q, name)
