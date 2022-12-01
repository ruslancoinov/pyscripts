# Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
'''x, y = int(input('X: ')), int(input('Y: '))
if x > 0 and y > 0:
    print('First quarter')
if x < 0 and y < 0:
    print('Second quarter')
if x < 0 and y < 0:
    print('Third quarter')
if x > 0 and y < 0:
    print('Fourth quarter')'''

'''x, y = int(input('X: ')), int(input('Y: '))
if x > 0:
    if y > 0:
        print('First quarter')
    else:
        print('Fourth quarter')
else:
    if y > 0:
        print('Second quarter')
    else:
        print('Fourth quarter')'''

# Программа, которая переводит стобалльную оценку в пятибалльную.
# Мы не могли написать 5 независимых if-ов, поскольку в таком случае было бы напечатано сразу несколько значений пятибалльной оценки.
'''grade = int(input('Введите вашу отметку по 100-балльной системе: '))
if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70: 
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)'''
# Предыдущий код можно переписать, используя каскадный условный оператор elif вмесето вложенного if-else.
'''grade = int(input('Введите вашу отметку по 100-балльной системе: '))
if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)'''
