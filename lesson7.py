# 1

class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


test_matrix = Matrix([
            [3, 5, 2],
            [2, 7, 1],
            [4, 1, 1],
        ], [
            [7, 5, 8],
            [8, 3, 9],
            [6, 9, 9],
        ]
)

print(test_matrix.__add__())

# 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(46)
suit = Suit(175)
print(coat + suit + coat)

# 3

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'The cell size is: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'The cell has become smaller, now its size is: {sub} to the cells '\
            if sub > 0 else 'The cell has disappeared!'

    def __truediv__(self, other):
        return f'The size of a common cell as a result of division: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'The size of the total cell as a result of multiplication: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(17)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(6))

