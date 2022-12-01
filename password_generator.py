import random
import colorama
colorama.init(autoreset=True)

NUMBERS, LETTERS_LOW, LETTERS_UP, SYMBOL, DOUBT_SYMBOL, chars = '0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^_', 'il1Lo0O', ''


def greeting():
    l = ['Welcome to Password Generator!', 'Developed by ......']
    for i in range(3):
        if i == 0 or i == 2:
            print(colorama.Fore.BLACK + '*' * (len(l[0]) + 4))
        else:
            print(colorama.Fore.BLACK + '*', l[0] + colorama.Fore.BLACK + ' *')
            print(colorama.Fore.BLACK + '*',
                  l[1] + ' ' * 12 + colorama.Fore.BLACK + '*')


def control_number(number):
    while True:
        if number.isdigit() and int(number) > 0:
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            number = input('Password quantity: ')
    return number


def control_length(length):
    while True:
        if length.isdigit() and int(length) > 0:
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            length = input('Password length: ')
    return length


def control_ask(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('One more try? (y/n): ')
    return ask


def control_ask_1(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Include numbers? (y/n): ')
    return ask


def control_ask_2(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Include lowercase letters? (y/n): ')
    return ask


def control_ask_3(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Include uppercase letters? (y/n): ')
    return ask


def control_ask_4(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Include symbols? (y/n): ')
    return ask


def control_ask_5(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Include ambiguous symbols (il1Lo0O)? (y/n): ')
    return ask


def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)

    return password


def generate_password_1(length, chars):
    chars = NUMBERS + LETTERS_LOW + LETTERS_UP + SYMBOL
    length = random.randrange(15, 30)
    password_1 = ''
    for i in range(chars):
        password_1 += random.choice(chars)
    return password_1


def fast_password(ask):
    while True:
        if ask == 'y':
            chars = NUMBERS + LETTERS_LOW + LETTERS_UP + SYMBOL
            length = random.randrange(15, 30)
            password_1 = ''
            for i in range(length):
                password_1 += random.choice(chars)
            print(password_1)
            break
        if ask == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Fast&Strong [y] or Choice [n]: ').lower()
    return ask


greeting()

while True:
    ask = input('Fast&Strong [y] or Choice [n]: ').lower()
    ask = fast_password(ask)
    if ask == 'y':
        ask = input('One more try? (y/n): ')
        ask = control_ask(ask)
        if ask == 'n':
            break

    else:
        number = input('Password quantity: ')
        number = control_number(number)
        number = int(number)
        length = input('Password length: ')
        length = control_length(length)
        length = int(length)
        ask1 = input('Include numbers? (y/n): ')
        ask1 = control_ask_1(ask1)
        if ask1.lower() == 'y':
            chars += NUMBERS
        ask2 = input('Include lowercase letters? (y/n): ')
        ask2 = control_ask_2(ask2)
        if ask2.lower() == 'y':
            chars += LETTERS_LOW
        ask3 = input('Include uppercase letters? (y/n): ')
        ask3 = control_ask_3(ask3)
        if ask3.lower() == 'y':
            chars += LETTERS_UP
        ask4 = input('Include symbols? (y/n): ')
        ask4 = control_ask_4(ask4)
        if ask4.lower() == 'y':
            chars += SYMBOL
        ask5 = input('Include ambiguous symbols (il1Lo0O)? (y/n): ')
        ask5 = control_ask_5(ask5)
        if ask5.lower() == 'n':
            for c in 'il1Lo0O':
                # to replace - variable chars is necessary!
                chars = chars.replace(c, '')
        if chars == '':
            print(colorama.Fore.LIGHTRED_EX + 'Nothing to generate!')
        else:
            for _ in range(number):
                print(generate_password(length, chars))
        ask = input('One more try? (y/n): ')
        ask = control_ask(ask)
        if ask == 'n':
            break
        else:
            chars = ''
