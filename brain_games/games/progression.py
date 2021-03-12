import prompt
from random import randint, randrange
name = prompt.string('May I have your name? ')


def winner_or_loser(q, name):
    if q == 3:
        return print("Congratulations, {}!".format(name))


def find_progression(name):
    q = 0
    counter = 3
    print('What number is missing in the progression?')
    while counter > 0:
        n = randint(5, 10)  # кол-во символов в прогрессии
        d = randint(1, 5)  # разница между числами прогрессии
        a = randint(1, 50)  # первое число прогрессии
        row = list(range(a, a + d * (n - 1) + d, d))
        new_element = row.index(randrange(a, row[-1], d))
        number = row[new_element]  # число, которое сравниваем с ответом
        row[new_element] = '..'
        print('Question: {}'. format(' '.join(map(str, row))))
        text = input("Answer: ")
        if text == str(number):
            print("Correct!")
            q += 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}. "
                  "\nLet's try again, {}!".format(text, str(number), name))
            return
        counter -= 1
    winner_or_loser(q, name)


find_progression()
