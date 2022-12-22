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
