# Only 1, 5, 10 and 25 coins allowed.
# What's min coins amount need to pay?
num = int(input('Price per Witcher\'s service: '))
counter = 0
while num >= 25:
    counter += 1
    num = num - 25
while num >= 10:
    counter += 1
    num = num - 10
while num >= 5:
    counter += 1
    num = num - 5
while num >= 1:
    counter += 1
    num = num - 1
print(counter)
