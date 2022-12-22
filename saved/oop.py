# 1
class Lion:
    def roar(self):
        print('Rrrrrr!!!')


a = Lion()
a.roar()

# 2. methods, self


class Counter:
    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f'Current counter value = {self.value}')

    def reset(self):
        self.value = 0

# 3


class Point:
    def set_coordinates(self, x, y):
        self.x, self.y = x, y

    def get_distance(self, point):
        if isinstance(point, Point):
            return (point.x ** 2 + point.y ** 2) ** 0.5
        else:
            print('Invalid value!')

# 4. __init__


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

# 5


class SoccerPlayer:
    def __init__(self, name='Leo', surname='Messi', goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, amount_goals=1):
        self.goals += amount_goals

    def make_assist(self, amount_assists=1):
        self.assists += amount_assists

    def statistics(self):
        print(
            f'{self.name} {self.surname} - goals: {self.goals}, assists: {self.assists}')

# 6


class Person:
    def __init__(self, name, surname, age):
        self.name, self.surname, self.age = name, surname, age

    def full_name(self):
        return f'{self.name} {self.surname}'

    def is_adult(self):
        return self.age >= 18

# 7


class Zebra:
    def __init__(self):
        self.count = 0

    def which_stripe(self):
        if self.count % 2 == 0:
            print('white line')
        else:
            print('black line')
        self.count += 1

# 8


class Dog:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sounds):
        return f'{self.name} says {sounds}'

# 9. stack


class Stack:
    def __init__(self):
        self.value = []

    def push(self, item):
        self.value.append(item)

    def pop(self):
        if len(self.value) != 0:
            removed = self.value.pop()
            return removed
        else:
            print('Empty stack')

    def peek(self):
        if len(self.value) != 0:
            return self.value[-1]
        else:
            print('Empty stack')
            return None

    def is_empty(self):
        return len(self.value) != 0

    def size(self):
        return len(self.value)

# 10. private attr


class Student:
    def __init__(self, name, age, branch):
        self.__name, self.__age, self.__branch = name, age, branch

    def __display_details(self):
        print(f'Name: {self.__name}')
        print(f'Age: {self.__age}')
        print(f'Branch: {self.__branch}')

    def access_private_method(self):
        self.__display_details()

# 11. get-method, set-method, property


class UserMail:
    def __init__(self, login, email):
        self.login, self.__email = login, email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) and email.count('@') == 1 and '.' in email[email.find('@'):]:
            self.__email = email
        else:
            print(f'ErrorMail: {email}')
    email = property(fget=get_email, fset=set_email)
