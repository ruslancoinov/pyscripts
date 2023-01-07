#!/usr/bin/python3

from time import monotonic


def translit(text):

    capital_letters = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sch',
        'Ъ': '',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Y',
        'Я': 'Ya',
    }

    lower_case_letters = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'y',
        'я': 'ya',
    }

    output_string = ''

    start = monotonic()

    for char in text:
        if char in capital_letters.keys():
            char = capital_letters[char]
        elif char in lower_case_letters.keys():
            char = lower_case_letters[char]
        output_string += char

    finish = monotonic()

    print()

    return output_string, f'{round(finish - start, 5)} sec'


def main():
    input_string = input('Please, input your text below\n>>> ')
    result = translit(input_string)
    print(
        f'{result[0]}\n\nAmount of sybols: {len(input_string)}; Total uptime: {result[1]}'
    )
    print()


if __name__ == '__main__':
    main()
