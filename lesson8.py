# 1

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'It is okay, the date exists!'
                else:
                    return f'The year is incorrect!'
            else:
                return f'The month is specified incorrectly!'
        else:
            return f'The day is specified incorrectly!'

    def __str__(self):
        return f'Current date{Data.extract(self.day_month_year)}'


today = Data('3 - 11 - 2021')
print(today)
print(Data.extract('11 - 11 - 2021'))
print(today.extract('8 - 10 - 2023'))
print(Data.valid(15, 12, 2022))
print(today.valid(3, 14, 2021))
print(Data.valid(3, 9, 1988))

# 2
class DivisionByZero(Exception):
    def __str__(self):
        return f'Division by zero is impossible!!'


# class D:
def calculation(x, y):
    if y == 0:
        return DivisionByZero(f'Division by zero is prohibited!')
    else:
        return x / y


print(calculation((int(input('Enter x: '))), (int(input('Enter y: ')))))

# 3

class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Enter a number or "stop" to exit:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as e:
        print('Is not a number!', e)
print(my_list)

# 4/ 5/ 6

#Если можно сдам до конца недели.

# 7

import math


class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(2, 3)
z2 = MyComplex(4, 1)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)


x = MyComplex(-3, 5)
y = MyComplex(2, 1)
print(x + y)
print(x * y)
