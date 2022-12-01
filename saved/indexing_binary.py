# Algorithm to convert decimal to binary
num = int(input('INT number in decimal system: '))
b = ''
while num != 0:
    a = num % 2
    b += str(a)
    num //= 2
for index in range(-1, -len(b) - 1, -1):
    print(b[index], end='')


# Format strings algorithm
a = input()[::-1]
d = 0
if len(a) > 3:
    for i in range(3, len(a), 3):
        a = a[:i + d] + ',' + a[i + d:]
        d += 1
print(a[::-1])

#Virus
for i in range(int(input())):
    s, virus, n = input(), 'anton', 0
    for c in s:
        if c in virus[n]:
            n += 1
        if n == 5:
            print(i + 1, end='')
            break