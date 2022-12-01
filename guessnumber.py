# 1.0 version and probably last one as point?
# Issues: when invalid character, it returns 'Guess number' instead of the text that is above
import colorama
colorama.init(autoreset=True)


def number_control(number):
    while True:
        if number.isdigit() and 0 < int(number) <= 100:
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            number = input('Guess number: ')
    return number


def ask_control(ask):
    while True:
        if ask.lower() == 'y' or ask == 'n':
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + 'Invalid character!')
            ask = input('Wanna play again? (y/n): ')
    return ask


def greeting():
    l = ['Welcome to guess game!',
         'Try guess random number from 1 to 100 for 7 attempts OR you lose']
    for i in range(3):
        if i == 0 or i == 2:
            print('*' * (len(l[1]) + 4))
        else:
            print('*', l[0], ' ' * 41, '*')
            print('*', l[1], '*')


greeting()
print('Let\'s go!')
print()
while True:
    from random import randrange
    count = 1
    random_number = randrange(1, 100)
    user_number = input('Guess number: ')
    user_number = number_control(user_number)
    user_number = int(user_number)
    while True:
        if user_number > random_number:
            count += 1
            if count == 5 or count == 6:
                print('(' + str(8 - count), 'attempts left' + ')', end=' ')
            elif count == 7:
                print('(' + str(8 - count), 'attempts left' + ')', end=' ')
            if count == 8:
                print(colorama.Fore.LIGHTYELLOW_EX + 'Game over. You lose. ' +
                      'That was ' + str(random_number) + '.')
                break
            user_number = input('Too much, try one more time: ')
            user_number = number_control(user_number)
            user_number = int(user_number)
        elif user_number < random_number:
            count += 1
            if count == 5 or count == 6:
                print('(' + str(8 - count), 'attempts left' + ')', end=' ')
            elif count == 7:
                print('(' + str(8 - count), 'attempts left' + ')', end=' ')
            if count == 8:
                print(colorama.Fore.LIGHTYELLOW_EX + 'Game over. You lose. ' +
                      'That was ' + str(random_number) + '.')
                break
            user_number = input('Too little, try one more time: ')
            user_number = number_control(user_number)
            user_number = int(user_number)
        else:
            print(colorama.Fore.LIGHTMAGENTA_EX + 'You are right with ' +
                  str(count) + ' attempt. ' + 'Congrats!')
            break
    ask = input('Wanna play again? (y/n): ')
    ask = ask_control(ask)
    if ask.lower() == 'n':
        break
