# 1

from sys import argv


def salary():
    try:
        output_in_hours, rate_per_hour, bonus = argv[1:]

        print(f"Salary: {float(output_in_hours) * float(rate_per_hour) + float(bonus)}")
    except ValueError:
        print("Enter all numbers.There can't be a string or an empty character!")


salary()

# 2

import random
initial_list = random.sample(range(1, 1000), 10)
result_list = [number for i, number in enumerate(initial_list) if i > 0 and initial_list[i] > initial_list[i - 1]]
print(initial_list)
print(result_list)

# 3

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# 4

from random import randint

list_1 = [randint(-10, 10)for _ in range(20)]
list_2 = [el for el in list_1 if list_1.count(el) == 1]
print(list_1)
print(list_2)

# 5

from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


even_num_list = [el for el in range(100, 1001, 2)]
multiplication_result = reduce(my_func, even_num_list)


print(even_num_list)
print(multiplication_result)

# 6

from itertools import islice, count, cycle


def arbitrary(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        new_list = [el for el in islice(count(), start_el, stop_el + 1)]
        rep_list = [el for el in islice(cycle(new_list), num_str)]
        print(new_list)
        return rep_list
    except ValueError:
        return "Error!"
    except TypeError:
        return "Error type!"


print(arbitrary(input("Start with: "), input("to: "), input("Нow many repetitions? ")))

# 7


def factorial(n):
    result = 1
    for i in range(n + 1):
        yield result
        result *= i+1


for el in factorial(int(input("Enter number: "))):
    print(el)
