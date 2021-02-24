import prompt


name = prompt.string('May I have your name? ')


def welcome_user(name):
    print('Hello, {}!'.format(name))


welcome_user(name)
