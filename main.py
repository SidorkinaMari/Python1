# 1.py. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = "Welcome"
b = "home!"
print(f"{a}, {b}")
num_1 = int(input("Enter number: "))
num_2 = int(input("Enter other number: "))
print(f"Your numbers are {num_1} and {num_2}")
word = input("What do you see in the window (one word): ")
print(f"In the window I see {word}.")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Enter integer: ")
while n < '0':
    print("Please enter number greater than 0!")
    n = input('Please try again: ')
print(f"{n} + {n+n} + {n+n+n} = {int(n) + int(n + n) + int(n +n + n)}")

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

num = int(input("Enter positive integer: "))
maximum = 0
while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
        if maximum == 9:
            break
    num = num // 10
print(f"The maximum digit in the number {num} is {maximum}")

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Enter the amount of revenue: "))
costs = float(input("Enter the cost amount: "))
result = revenue - costs
if result > 0:
    print(f"Your company operates with a profit equal to {result}.")
    print(f"The profitability of revenue is {100 * result / revenue:.1f}%")
    employees = int(input("How many employees work in the company? "))
    print(f"If you divide the profit between employees, then everyone will receive {result / employees:.3f}.")
elif result < 0:
    print(f"Unfortunately, the company is operating at a loss of {-result}.")
else:
    print("Welcome to the break-even point!")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    first_result = float(input("Starting result: "))
    last_result = float(input("Final result: "))
    days = 1
    if first_result <= 0 or last_result < 0:
        print("The first result cannot be zero! Both results must be greater than zero!")
    else:
        while first_result < last_result:
            first_result += first_result * 0.1
            days +=1
        print(f"The athlete will achieve the result in {days} days.")
        break

