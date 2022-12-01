# 1
'''n = int(input())
s = ''
for i in range(n):
    s += chr(97 + i)
print(list(s))'''

n = int(input())
s = ''
for i in range(97, 123):
    s += chr(i)
print(list(s)[:n])

n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
print(l)

# 2
l = []
for i in range(26):
    l += chr(97 + i)
l1 = []
n = 1
for i in l:
    l1.append(i * n)
    n += 1
print(l1)
print(len(l1[-1]))
