# 1

from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(9)
            i += 1


t = TrafficLight()
t.running()

# 2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'It takes {round(asphalt_mass)} to cover the entire roadway')


r = Road(5000, 20)
r.asphalt_mass()

# 3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Vasilisa', 'Petrova', 'SMM', '85000', '20000')
print(p.get_full_name(), p.get_total_income())

# 4

from random import choice


class Car:
    direction = ['north', 'east', 'south', 'west']

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'This is a {name} {color} car. Is it the police? {is_police}')

    def go(self):
        print(f'The {self.name} went.')

    def stop(self):
        print(f'The {self.name} has stopped.')

    def turn(self):
        print(f'The {self.name} turned {choice(self.direction)}.')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'This speed is  {self.speed}, it is higher than allow! '
        else:
            return f'Speed of {self.name} is normal'


class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return f'This speed is  {self.speed}, it is higher than allow! '
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police=True)


town_car = TownCar('KIA', 'black', 57)
work_car = WorkCar('Ford Transit', 'blue', 45)
sport_car = SportCar('Ferrari', 'red', 148)
police_car = PoliceCar('Ford', 'white', 80)

list_cars = [town_car, work_car, sport_car, police_car]

for i in list_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

# 5
class Stationery:
    def __init__(self, title='Subject for drawing'):
        self.title = title

    def draw(self):
        return f'Starting rendering!{self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Starting rendering with a {self.title} pen.'


class Pencil(Stationery):
    def draw(self):
        return f'Starting rendering with a {self.title} pencil.'


class Handle(Stationery):
    def draw(self):
        return f'Starting rendering with a {self.title} handle.'


pen = Pen('Parker')
print(pen.draw())
pencil = Pencil('KOH-I-NOOR')
print(pencil.draw())
handle = Handle('COPIC')
print(handle.draw())