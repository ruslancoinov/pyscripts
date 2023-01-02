# Трибоначи - последовательность, где число равно сумме трех предыдущих.
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3

# 2
s = input()
print('YES' if len(s) == len(set(s)) else 'NO')
# one more solve
s = input()
print(('NO', 'YES')[len(s) == len(set(s))])

# Find all that there're in n and not in m
n, m = [set([int(c) for c in input().split()]) for _ in range(2)]
print(*sorted(n - m))

# 3 Find all students who were on each lesson
m = int(input())  # amount of lessons
l = {input() for _ in range(int(input()))}  # students present on lesson

for _ in range(m - 1):  # Compare other lessons with first =>' m - 1'
    # update first set by adding new students on intersection
    l.intersection_update([input() for _ in range(int(input()))])

print(*sorted(l), sep='\n')

# 4
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098',
             'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'}]

# Names that has no email
k = [d['name'] for d in users if 'email' not in d or d['email'] == '']
print(*sorted(k))

# 5 Count how many time each number in list repeats
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10,
           4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:  # Create key=num and its value
    # If value in result=> value else 0 + 1
    result[num] = result.get(num, 0) + 1

# 6
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65)]
result = {}  # Make tuples 0f names of hosts with list of dogs
for t in pets:
    result.setdefault(t[1:], []).append(t[0])

# 7
l = [c.strip('.,!?:;-,') for c in input().lower().split()]

my_dict = {}

for n in l:
    my_dict[n] = my_dict.get(n, 0) + 1

# s = {key for key in my_dict if my_dict[key] == min(my_dict.values())}
# print(sorted(s)[0])
my_list = [(value, key) for key, value in my_dict.items()]
my_list.sort()
print(my_list[0][1])


# 8 if dictionary needed: key-value
res = {}
for _ in range(int(input())):
    key, value = input().split()
    res[key.capitalize()] = value.capitalize()


# 9
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35,
           95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

# dict of numbers in numbers whith value of list with its seperators
result = {i: sorted([int(i / j)
                    for j in range(1, i + 1) if i % j == 0]) for i in numbers}


# 10
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006',
               'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle',
                 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain',
                 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen',
                 'Gary Oldman', 'Tom Hardy']

student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{student_ids: {student_names: student_grades}} for student_ids,
          student_names, student_grades in zip(student_ids, student_names, student_grades)]
