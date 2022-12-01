# Does the specified number consist of same digit?
num = int(input('Does your number consist of same digit? '))
a = 9
b = 0  # max
while num != 0:
    last_digit = num % 10
    if last_digit < a:
        a = last_digit
    if last_digit > b:
        b = last_digit
    num = num // 10
if a == b:
    print('YES')
else:
    print('NO')
