from math import sqrt
__author__ = 'Кравченко Сергей'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Figure:

    @property
    def perimeter(self):
        return sum(self.sides.values())


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.sides = {}
        self.sides['1'] = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.sides['2'] = sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.sides['3'] = sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return sqrt(half_perimeter * (half_perimeter - self.sides['1']) *
                    (half_perimeter - self.sides['2']) *
                    (half_perimeter - self.sides['3']))

    @property
    def height(self):
        return self.area * 2 / self.sides['2']    


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Figure):
    def __init__(self, a, b, c, d):
        self.sides = {}
        self.sides['1'] = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.sides['2'] = sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.sides['3'] = sqrt((d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2)
        self.sides['4'] = sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2)
        self.diagonal_1 = sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
        self.diagonal_2 = sqrt((b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2)

    @property
    def equilateral(self):
        return self.diagonal_1 == self.diagonal_2

    @property
    def area(self):
        height = sqrt(self.sides['1'] ** 2 -
                      ((self.sides['4'] - self.sides['2']) / 2) ** 2)
        return (self.sides['2'] + self.sides['4']) * height / 2


if __name__ == '__main__':
    # Задача-1
    triangle = Triangle((0, 0), (4, 0), (0, 3))
    print('Периметр треугольника: {:.2f}'.format(triangle.perimeter))
    print('Площадь треугольника: {:.2f}'.format(triangle.area))
    print('Высота треугольника опущенная из вершины A: {:.2f}'.format(
        triangle.height))
    # Задача-2
    trapezium = Trapezium((0, 0), (1, 5), (5, 5), (6, 0))
    if trapezium.equilateral:
        print('Трапеция является равнобочной')
    else:
        print('Трапеция не равнобочная')
    print('Длина стороны AB: {:.2f}'.format(trapezium.sides['1']))
    print('Длина стороны BC: {:.2f}'.format(trapezium.sides['2']))
    print('Длина стороны CD: {:.2f}'.format(trapezium.sides['3']))
    print('Длина стороны DA: {:.2f}'.format(trapezium.sides['4']))
    print('Периметр трапеции: {:.2f}'.format(trapezium.perimeter))
    print('Площадь трапеции: {:.2f}'.format(trapezium.area))


