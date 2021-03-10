import math


def quadratic(a, b, c):
    """Calculates quadratic equation root(s) for given values (imaginary solution are omitted)"""
    d = b ** 2 - 4 * a * c  # discriminant

    if d < 0:
        print("This equation has no real solution")
    elif d == 0:
        x = (-b + math.sqrt(d)) / 2 * a
        print(round(x, 2))
        return round(x, 2)

    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(round(x1, 2), round(x2, 2))
        return round(x1, 2), round(x2, 2)
