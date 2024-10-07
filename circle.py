import math


def area(r):
    '''
        Вычисляет площадь круга.

        Параметры:
        r (float): Радиус круга.

        Возвращаемое значение:
        float: Площадь круга, вычисленная по формуле π * r².

        Пример:
        >>> area(5)
        78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Вычисляет периметр круга.

        Параметры:
        r (float): Радиус круга.

        Возвращаемое значение:
        float: Периметр круга, вычисленный по формуле 2 * π * r.

        Пример:
        >>> perimeter(5)
        31.41592653589793
    '''
    return 2 * math.pi * r

