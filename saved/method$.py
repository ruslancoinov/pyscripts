# Algorithm to count words in string.
a = input().lower()
b = a.count(' ') + 1
print(b)

# Алгоритм подсчета самого посторяющегося символа в строке.
word = input('Any word containing any symbols: ')
count, mvx = 0, 0
for letter in word:
    if word.count(letter) >= count:  # Перебирает кол-во символа в строке word.
        count = word.count(letter)  # Записывает кол-во в count
        mvx = letter  # Какой именно символ.
print(mvx)

# format method
age = 27
name = 'Realone'
job = 'Dealer'
txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, job)  # ALLOW: txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, job) AND: txt = 'My name is {0}-{0}-{0}'.format(name)
print(txt)

# F-str, when many parameters under format method, put f before '' and name var. in {}
first_name, last_name, age, profession, affiliation = 'blvmme', 'Arranovski', 20, 'bomj', 'Fvctotum'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')

# Cesar cipher decryption
n = int(input('Step from 1 to 25'))
s = input('Cipher phrase: ')
for letter in s:
    foo = ord(letter) - n
    if foo < 97:
        foo += 26
    print(chr(foo), end='')
