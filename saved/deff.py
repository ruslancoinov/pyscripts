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
