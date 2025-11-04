import pytest

from main import discriminant, solution

test_cases_for_discriminant = [
    (1, 8, 15, 4),
    (1, -13, 12, 121),
    (-4, 28, -49, 0),
    (1, 1, 1, -3)
]
test_cases_for_solution = [
    (1, 8, 15, (-3.0, -5.0)),
    (1, -13, 12, (12.0, 1.0)),
    (-4, 28, -49, 3.5),
    (1, 1, 1, 'корней нет')
]

@pytest.mark.parametrize("a, b, c, expected", test_cases_for_discriminant)
def test_discriminant(a, b, c, expected):
    """
    Проверяем, что функция discriminant() правильно вычисляет дискриминант
    """
    assert discriminant(a, b, c) == expected

@pytest.mark.parametrize("a, b, c, expected", test_cases_for_solution)
def test_quadratic_equation(a, b, c, expected):
    """
    Проверяем, что функция solution() правильно решает квадратное уравнение
    """
    assert solution(a, b, c) == expected

if __name__ == '__main__':
    test_discriminant()
    test_quadratic_equation()