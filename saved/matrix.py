# 1
n, m = int(input()), int(input())
matrix = [[None] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for r in range(n):  # Output
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
print()
for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

# 2
matrix = []
for r in range(n):
    row = [input() for _ in range(m)]
    matrix.append(row)
print(matrix)

# 3
matrix = [[int(c) for c in input().split()] for _ in range(n)]
matrix = [input.split() for _ in range(n)]
for row in matrix:
    print(*row)

# 4 Multiple
n, m = [int(c) for c in input().split()]
matrix1 = [[int(c) for c in input().split()] for _ in range(n)]
input()
m, k = [int(c) for c in input().split()]
matrix2 = [[int(c) for c in input().split()] for _ in range(m)]
matrix3 = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix3[i][j] += matrix1[i][x] * matrix2[x][j]
for row in matrix3:
    print(*row)


# 5 Bingo board
from random import sample

# all numbers are different and 0 in the center
numbers = sample(range(1, 56), 25)
card = [[numbers.pop() for _ in range(5)] for _ in range(5)]
card[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(card[i][j]).ljust(3), end='')
    print()
