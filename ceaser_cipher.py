# # # # # # # # # # # # # # # # # # # # # # # # #
#           CEASER CIPHER ALGORITHM             #
# # # # # # # # # # # # # # # # # # # # # # # # #

def is_int(key):
    try:
        int(key)
        return True
    except ValueError:
        return False


def control_e(text):
    text = text.replace('Ё', 'Е')
    text = text.replace('ё', 'е')
    return text


def control_text(text):
    while True:
        if text.isspace() or text == '' or text.isdigit():
            text = input('Input text below:\n')
        else:
            break
    return text


def ceaser_cipher(key, text):
    result, n = [], ''
    abc_upper_ru, abc_lower_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    abc_upper_en, abc_lower_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(text)):
        if text[i] in abc_upper_ru:
            n = abc_upper_ru
        elif text[i] in abc_lower_ru:
            n = abc_lower_ru
        elif text[i] in abc_upper_en:
            n = abc_upper_en
        elif text[i] in abc_lower_en:
            n = abc_lower_en
        else:
            result.append(text[i])

        if text[i] in n:
            for j in range(len(n)):
                if text[i] == n[j]:
                    result.append(n[(j + int(key)) % len(n)])
    return ''.join(result)


def control_ask(ask):
    while True:
        if ask.lower() == 'y' or ask.lower() == 'n':
            break
        else:
            ask = input('One more try? (y/n): ')
    return ask


# def ceaser_cipher(text):
#     result, n = [], ''
#     abc_upper_ru, abc_lower_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#     abc_upper_en, abc_lower_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'

#     for i in range(len(text)):
#         if text[i] in abc_upper_ru:
#             n = abc_upper_ru
#         elif text[i] in abc_lower_ru:
#             n = abc_lower_ru
#         elif text[i] in abc_upper_en:
#             n = abc_upper_en
#         elif text[i] in abc_lower_en:
#             n = abc_lower_en
#         else:
#             result.append(text[i])

#         if text[i] in n:
#             for j in range(len(n)):
#                 if text[i] == n[j]:
#                     result.append(n[(j + key) % len(n)])
#     return ''.join(result)

# for key in range(-32, 32):
#     print(ceaser_cipher('Hawnj pk swhg xabkna ukq nqj.'))


while True:
    text = input('Input text below:\n')
    text = control_text(text)

    key = input('Desired key? (pos./neg.)\n')
    while is_int(key) != True:
        key = input('Desired key? (pos./neg.)\n')

    print(ceaser_cipher(key, text))

    ask = input('One more try? (y/n): ')
    ask = control_ask(ask)
    if ask == 'n':
        break
