auto = ['Toyota', 'Volkswagen', 'Nissan', 'Honda', 'Ford', 'Chrysler', 'Hyundai', 'Ram', 'Porsche', 'Tesla', 'Mitsubishi', 'Mercedes',
        'BMW', 'Lexus', 'Chevrolet', 'Audi', 'Kia', 'Volvo', 'Infiniti', 'Mazda', 'Subaru', 'Kia', 'Jaguar', 'Dodge', 'Cadillac']


def display_hangman(tries):
    stages = [
        '''
        ------
        |    |
        |    O
        |   \|/
        |    |
        |   / \\
        _
                ''',

        '''
        ------
        |    |
        |    O
        |   \|/
        |    |
        |   / 
        _
                ''',

        '''
        ------
        |    |
        |    O
        |   \|/
        |    |
        |   
        _
                ''',

        '''
        ------
        |    |
        |    O
        |   \|
        |    |
        |    
        _
                ''',

        '''
        ------
        |    |
        |    O
        |    |
        |    |
        |   
        _
                ''',

        '''
        ------
        |    |
        |    O
        |   
        |    
        |    
        _
                ''',

        '''
        ------
        |    |
        |    
        |   
        |    
        |   
        _
                '''  # Use \\ for screening

    ]
    return stages[tries]


import random


def get_word():
    word = random.choice(auto).upper()
    return word


def print_word_completion(word, list):
    for c in word:
        if c in list:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def play_again():
    while True:
        ask = input('One more try? [y]/[n]: ').lower()
        if ask == 'y':
            break
        elif ask == 'n':
            break
        else:
            print('Invalid character!')
            continue
    return ask


def play(word):
    word_completion = '_ ' * len(word)
    tries = 6
    guessed_letters = []
    guessed_words = []
    flag = False
    print(display_hangman(tries))
    print(word_completion)
    while True:
        user_input = input('Enter letter or full word: ').upper()

        if user_input in guessed_words or user_input in guessed_letters:
            print('Already exist!')
            continue
        if not user_input.isalpha():
            print('Invalid character!')
            continue

        if len(user_input) > 1:
            if word == user_input:
                print('Congratulations! You are right')
                break
            else:
                guessed_words.append(user_input)
                tries -= 1
                print(display_hangman(tries))
                print(f'Miss! {tries} tries left')
                if tries == 0:
                    print(
                        f'Unfortunately, you couldn\'t guess the word. It was {word}')
                    break
                continue
        if len(user_input) == 1:
            if user_input in word:
                guessed_letters.append(user_input)
                for c in word:
                    if c not in guessed_letters:
                        print('Exactly!')
                        print_word_completion(word, guessed_letters)
                        flag = False
                        break
                    flag = True
                if flag:
                    print_word_completion(word, guessed_letters)
                    print('Congratulations! You are right.')
                    break
            else:
                guessed_letters.append(user_input)
                tries -= 1
                print(display_hangman(tries))
                print(f'Miss! {tries} tries left')
                print_word_completion(word, guessed_letters)
                if tries == 0:
                    print(
                        f'Unfortunately, you couldn\'t guess the word. It was {word}')
                    break
                continue


while True:
    play(get_word())
    ask = play_again()
    if ask == 'y':
        continue
    else:
        break
