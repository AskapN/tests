def discriminant(a, b, c):
    """
    Функция для нахождения дискриминанта
    """
    d = b ** 2 - 4 * a * c
    return d

def solution(a, b, c):
    """
    Функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return 'корней нет'
    elif d == 0:
        x = (-b + d ** 0.5) / (2 * a)
        return x
    else:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
    return x_1, x_2


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)