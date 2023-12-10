import math


def solve_quadratic(a, b, c):

    assert isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (
    int, float)), "Коефіцієнти повинні бути числами"
    assert a != 0, "Це не квадратне рівняння (a не може дорівнювати нулю)"


    discriminant = b ** 2 - 4 * a * c


    assert discriminant >= 0, "Рівняння не має розв'язків на множині дійсних чисел"


    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return x1, x2



a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))


try:
    solution = solve_quadratic(a, b, c)
    print("Розв'язки рівняння:", solution)
except AssertionError as e:
    print("Помилка:", e)
