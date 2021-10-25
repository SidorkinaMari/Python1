# 1

with open('new.txt', 'w', encoding='utf-8') as nf:
    while True:
        line = input('Enter a line or an empty line to end. ')
        if not line:
            break
    nf.write(f'{line}\n')

    nf.close()

# 2

with open('text_4.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Number of lines in the file: {len(my_list)}. There are {len(new_l)} words in the {i + 1} line.')

    f.close()

# 3

with open('text_3.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    sum = 0
    for row in lines:
        line = row.split()

        if float(line[1]) < 20000:
            print(f'{line[0]} has a salary of less than 20 000 rubles.')

        sum += float(line[1])

    print(f'The average earnings of employees amounted to: {sum/len(lines)} rubles')

    f.close()

# 4

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w') as f_2:
    f_2.writelines(new_file)

    f.close()
    f_2.close()

# 5

from random import randint

with open('file_5.txt', 'w', encoding='utf-8') as f:
    my_list = [randint(1, 100) for _ in range(100)]
    f.write(" ".join(map(str, my_list)))

print(f'The sum of all elements is equal to: {sum(my_list)}')

f.close()

# 6

subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, information = line.split(':')
        sum_by_name = sum(map(int, "".join([i for i in information if i == ' ' or '9' >= i >= '0']).split()))
        subj[name] = sum_by_name
    print(f'Total number of hours per subject: {subj}')

    f.close()

# 7

import json

with open('file_7.json', 'w', encoding='utf-8') as fj:
    with open('text_7.txt', encoding='utf-8') as f:
        income = {line.split()[0]: int(line.split()[3]) for line in f}
        breakeven = [int(i) for i in income.values() if int(i) > 0]
        result = [income, {'average_profit ': round(sum(breakeven) / len(breakeven))}]
    json.dump(result, fj, ensure_ascii=False, indent=4)
