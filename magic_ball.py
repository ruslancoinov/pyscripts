print('''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#     Welcome to Magic Ball! It can predict any question you have.    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
''')


def name_control(name_user):
    while True:
        if name_user.isspace() or name_user == '':
            print('It doesn\'t look like a name at all')
            name_user = input('How to reference to you? ')
        else:
            break
    return name_user


def question_control(question):
    while True:
        if question.isspace() or question == '':
            print('It doesn\'t look like a question at all')
            question = input('Your question: ')
        else:
            break
    return question


def ask_control(ask):
    while True:
        if ask.lower() == 'y' or ask == 'n':
            break
        else:
            print('Invalid character!')
            ask = input('One more question? (Y/N): ')
    return ask


answers = ["Indisputably", "Predetermined", "No doubt", "Definitely yes", "You can be sure of it", "It seems to me - yes", "Most likely", "Good prospects", "Signs say - yes", "Yes", "It's not clear yet, try again",
           "Ask later", "It's better not to tell", "It's impossible to predict now", "Concentrate and ask again", "Don't even think", "My answer is no", "According to my data - no", "Prospects are not very good", "Very doubtful"]


name_user = input('How to reference to you? ')
name_user = name_control(name_user)

print(
    f'Okay, {name_user}. Ask me any question, e.g. "Will I become rich?" and similar\nAnd I will answer like "{answers[6]}" and similar.')
import time
import random
while True:
    question = input('Your question: ')
    question = question_control(question)
    answer = random.choice(answers)
    time.sleep(2)
    print(f'Here is the answer: {answer}')
    ask = input('One more question? (y/n): ')
    ask = ask_control(ask)
    if ask.lower() == 'n':
        print('Come back if question arises!')
        break
