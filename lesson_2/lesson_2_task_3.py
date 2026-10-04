import math


def square(side):
    area = side*side
    return math.ceil(area)


side_length = int(input('side:'))
print("Сторона:", side_length, "Площадь:", square(side_length))
