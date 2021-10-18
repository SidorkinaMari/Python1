#1

def calculation(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Mistake! Division by zero is impossible!')

print(calculation((int(input('Enter first number: '))), (int(input('Enter second number: ')))))

#2

def p_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Name: {name} Surname: {lastname} Birth year: {year_of_birth} '
                 f'City of residence: {city} E-mail: {email} Phone: {phone}')
p_data(
    name=input('Name: '),
    lastname=input('Surname: '),
    year_of_birth=input('Birth year: '),
    city=input('City of residence: '),
    email=input('E-mail: '),
    phone=input('Phone: '),
)

#3

def my_func(a, b, c):
    print(f'The sum of the two largest arguments is: {a + b + c - min([a, b, c])}')
my_func(
    int(input('Enter a:')),
    int(input('Enter b:')),
    int(input('Enter c:')),
)

#4.1

def my_func(x, y):
    return x ** y
print(f'Exponentiation of a number: '
      f'{my_func(int(input("Enter the degree base Х: ")), int(input("Enter the exponent Y: ")))}')

#4.2

def my_func(x, y):
    counter = 1
    # Для возведения в отрицательную степень нужно:
    # Записать число в виде дроби с единицой в числителе и с исходным числом в степени внизу
    # заменить отрицательную степень на положительную
    # возвести число в положительную степень
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result
print(f'Exponentiation of a number: '
      f'{my_func(int(input("Enter the degree base Х: ")), int(input("Enter the exponent Y: ")))}')

#5

def new_sum():
    s = 0
    while True:
        a = list(input('Enter numbers with space. Enter "#" for stop.: ').split())
        for num in a:
            if num == '#':
                return s
            else:
               try:
                 s += int(num)
               except ValueError:
                    print('Enter "#" for exit!')
            print(f'Sum of numbers = {s}')
print(new_sum())

#6.1

def int_func(text):
    return text.title()

print(int_func("text"))

#6.2

def my_text(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output = []
for word in input('Enter a string with words separated by spaces: ').split(' '):
    output.append(int_func(word))

print(f'{" ".join(output)}')
