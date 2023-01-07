# Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]
n = int(input())
print(get_factors(n))

# 2
print(*[int(i) ** 2 for i in input().split(' ') if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

# 3. Input n digits in format "1 2 3...n", merge all together.
def merge(list1, list2):
    l = list1 + list2
    l.sort()
    return l

total_list = []
for i in range(int(input())):
    l = [int(i) for i in input().split(' ')]
    total_list = merge(total_list, l)

print(*total_list)


# 4
# greet takes 1+ args
def greet(name, *args):
    return f'Hello, {" and ".join(((name,) + args))}!'


# 5. sort the list by categories
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
            ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# I)
def generator_comparator(value_of_tpl):
    def comparator(tpl):
        return tpl[value_of_tpl - 1]
    return comparator  # return comparator function
comp = generator_comparator(int(input()))
athletes.sort(key=comp)

# II)
def comparator(tpl):
    return tpl[value_of_tpl - 1]
value_of_tpl = input()
# needs to be not other name-so key won't see it, and function not see it local but see global
athletes.sort(key=comparator)


# 6. THINK ABOUT IT
import math

def pwr(p):
    def num_pwr(x):
        return x ** p
    return num_pwr

my_dict = {'квадрат': pwr(2), 'куб': pwr(3), 'корень': pwr(0.5), 'модуль': abs, 'синус': math.sin}

x, key = int(input()), input()

print(my_dict[key](x))
