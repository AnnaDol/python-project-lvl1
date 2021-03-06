import prompt
from random import randint
name = prompt.string('May I have your name? ')


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))


def find_gcd(name):
    q = 0
    counter = 3
    print('Find the greatest common divisor of given numbers.')
    while counter > 0:
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        print('Question: {} {}'.format(number_one, number_two))
        text = input("Answer: ")
        while number_one != 0 and number_two != 0:
            if number_one > number_two:
                number_one %= number_two
            else:
                number_two %= number_one
            gcd = number_one + number_two
        if text == str(gcd):
            print("Correct!")
            q += 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}. "
                  "\nLet's try again, {}!".format(text, str(gcd), name))
            return
        counter -= 1
    winner_or_loser(q, name)


find_gcd()
