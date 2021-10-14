#1
my_list = ['abrakadabra', 15, None, 5.3, (3+4j), -50, 'True']
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)

#2

list_from_input = [int(i) for i in input('Enter the numbers separated by a space: ').split()]
print(f'Your list {list_from_input}')
i = 0
while True:
    if i >= len(list_from_input) - 1:
        break
    list_from_input[i], list_from_input[i+1] = list_from_input[i+1], list_from_input[i]
    i += 2
print(f'New list: {list_from_input}')

#3

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Enter month number: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
    print("Error month number!")

#4

user_string = input("Enter a few words: ").split()
for w, i in enumerate(user_string, 1):
    print(w, i) if len(i) <= 10 else print(w, i[:10])

#5

my_list = [7, 5, 3, 3, 2]
print(f"rating - {my_list}")
digit = int(input("Enter any number (if enter 111 - end): "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"current list - {my_list}")
    digit = int(input("Enter next number (if enter 111 - end): "))

#6

products_list = []
i = 1
while True:
    products_list.append(
        (input('Enter item number: '), dict({
            'name': str(input('Enter name: ')),
            'price': float(input('Enter prise: ')),
            'quantity': int(input('Enter quantity: ')),
            'unit': str(input('Enter units of measurement: ')),
        }))
    )

    if input('The product has been added. Do you want to add another one? (y/N): ') == 'N':
        break

    i += 1

print(f'products list:{products_list}')

output_dict = dict({})
for product in products_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'Analytics collected: {output_dict}')
