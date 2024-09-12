import math
import opt


def f(x1, x2):
    return x1**4 + x2**4 - 4 * x1 * x2


def dfx1(x1, x2):
    return 4 * x1**3 - 4 * x2


def dfx2(x1, x2):
    return 4 * x2**3 - 4 * x1


def l(x1, x2):
    return math.sqrt(dfx1(x1, x2) ** 2 + dfx2(x1, x2) ** 2)


def fh(x1, x2, h):
    return (
        (x1 - h * (4 * x1**3 - 4 * x2)) ** 4
        + (x2 - h * (4 * x2**3 - 4 * x1)) ** 3
        - 4 * (x1 - h * (4 * x1**3 - 4 * x2)) * (x2 - h * (4 * x2**3 - 4 * x1))
    )


def gradient_descent():
    x0 = y0 = 0.5
    l = 0.1
    eps = 0.05
    while True:
        f0 = f(x0, y0)
        vfx = [dfx1(x0, y0), dfx2(x0, y0)]

        next_x = x0 - l * vfx[0]
        next_y = y0 - l * vfx[1]
        next_f = f(next_x, next_y)
        if abs(next_f - f0) <= eps:
            print(next_x, next_y)
            print(next_f)
            return
        x0 = next_x
        y0 = next_y


def fastest_descent():
    x0 = y0 = 0.5
    eps = 0.05
    while True:
        f0 = f(x0, y0)
        vfx = [dfx1(x0, y0), dfx2(x0, y0)]
        next_x = x0 - opt.perform_halving_division(fh, x0, y0) * vfx[0]
        next_y = y0 - opt.perform_halving_division(fh, x0, y0) * vfx[1]

        next_f = f(next_x, next_y)
        if abs(next_f - f0) <= eps:
            print(next_x, next_y)
            print(next_f)
            return
        x0 = next_x
        y0 = next_y


def solve():
    gradient_descent()
    fastest_descent()
