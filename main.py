class Coordinates:
    def __init__(self, *args):
        if len(args):
            self.points = sorted([elem for elem in args if isinstance(elem, int)])
        else:
            self.points = []
    def __str__(self):
        if len(self.points):
            return f"Координаты({', '.join(map(str, self.points))})"
        else:
            return "Пустые координаты"
    def __add__(self, other):
        if isinstance(other, int):
            temp = [i + other for i in self.points]
            return Coordinates(*temp)
        elif isinstance(other, Coordinates):
            if len(self.points) == len(other.points):
                temp = [i + j for i, j in zip(self.points, other.points)]
                return Coordinates(*temp)
            else:
                print("Сложение наборов разной длины невозможно")
                return None
        else:
            print(f"Невозможно сложить с {other}")
    def __mul__(self, other):
        if isinstance(other, int):
            return Coordinates([i * other for i in self.points])
        elif isinstance(other, Coordinates):
            if len(self.points) == len(other.points):
                temp = [i * j for i, j in zip(self.points, other.points)]
                return Coordinates(*temp)
            else:
                print("Умножение наборов разной длины невозможно")
                return None
        else:
            print(f"Невозможно умножить с {other}")
coords1 = Coordinates(1, 2, 3)
coords2 = Coordinates(3, 4, 5)
coords3 = coords1 + coords2
coords4 = coords3 + 5
coords5 = coords1 * 2

# Ассерты для проверки методов класса
assert str(coords1) == "Координаты(1, 2, 3)", 'Ошибка: метод __str__() объекта coords1 не возвращает "Координаты(1, 2, 3)".'
assert str(coords2) == "Координаты(3, 4, 5)", 'Ошибка: метод __str__() объекта coords2 не возвращает "Координаты(3, 4, 5)".'
assert str(coords3) == "Координаты(4, 6, 8)", 'Ошибка: метод __str__() объекта coords3 не возвращает "Координаты(4, 6, 8)".'
assert str(coords4) == "Координаты(9, 11, 13)", 'Ошибка: метод __str__() объекта coords4 не возвращает "Координаты(9, 11, 13)".'
assert str(coords5) == "Координаты(2, 4, 6)", 'Ошибка: метод __str__() объекта coords5 не возвращает "Координаты(2, 4, 6)".'
assert coords5 + 'hello' == "Невозможно сложить с hello", 'Ошибка: метод __add__() объекта coords5 не возвращает "Невозможно сложить с hello".'

# Проверка сложения с вектором разной длины
coords6 = Coordinates(1, 2)
assert (coords1 + coords6) == "Сложение наборов разной длины невозможно", 'Ошибка: метод __add__() для coords1 и coords6 не возвращает "Сложение наборов разной длины невозможно".'

# Проверка умножения с вектором разной длины
assert (coords1 * coords6) == "Умножение наборов разной длины невозможно", 'Ошибка: метод __mul__() для coords1 и coords6 не возвращает "Умножение наборов разной длины невозможно".'
print('Good')