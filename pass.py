#!/usr/bin/python3

from random import sample, choice, shuffle
from string import digits, ascii_lowercase, ascii_uppercase, punctuation


def generate_password(length):
    if length == '':
        new_digits = [c for c in digits if c not in '01']
        upper_letters = [c for c in ascii_uppercase if c not in 'IO']
        lower_letters = [c for c in ascii_lowercase if c not in 'ol']
        symbols = [c for c in punctuation if c not in '''`'"''']
        password = [choice(i) for i in (new_digits, ascii_lowercase, ascii_uppercase, symbols)] + \
            sample(new_digits + upper_letters +
                   lower_letters + symbols, 20 - 4)
    elif length < 5:
        password = [choice(i) for i in (
            digits, ascii_lowercase, ascii_uppercase, punctuation)]
        password = sample(password, length)
    else:
        password = [choice(i) for i in (
            digits, ascii_lowercase, ascii_uppercase, punctuation)]
        symbols = digits + ascii_lowercase + ascii_uppercase + punctuation
        for _ in range(length - 4):
            password.append(choice(symbols))

    shuffle(password)

    return ''.join(password)


def generate_passwords(amount, length):
    return [generate_password(length) for _ in range(amount)]


def user_amount():
    while True:
        amount = input('Amount: ')
        if amount == '':
            amount = '1'
        elif not amount.isdigit() or int(amount) < 1:
            continue
        break
    return int(amount)


def user_length():
    while True:
        length = input('Length: ')
        if length.isdigit() and int(length) > 0:
            return int(length)
        elif length == '':
            return length
        else:
            continue


print(*generate_passwords(user_amount(), user_length()), sep='\n')
