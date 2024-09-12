import math


def func(x):
    """
    Вычисляем значение функции, в качестве примера

    """
    try:
        result = 1 / x + pow(math.e, x)
        return result
    except OverflowError:
        print("Ошибка: выход за пределы допустимого диапазона. Округление числа.")
        return round(x, 2)  # Округляем число до двух знаков после запятой


def calculate_min_point(x_1, x_2, x_3, f_x1, f_x2, f_x3, delta_x):
    zero_checker = (x_2 - x_3) * f_x1 + (x_3 - x_1) * f_x2 + (x_1 - x_2) * f_x3
    if zero_checker == 0:
        recalculate(x_1, delta_x)
        return x_1
    min_point = 0.5 * (
        ((x_2**2 - x_3**2) * f_x1 + (x_3**2 - x_1**2) * f_x2 + (x_1**2 - x_2**2) * f_x3)
        / ((x_2 - x_3) * f_x1 + (x_3 - x_1) * f_x2 + (x_1 - x_2) * f_x3)
    )
    return min_point


def remove_max_1(a):
    a.pop(a.index(max(a)))


def recalculate(x_1, delta_x):
    x_2 = x_1 + delta_x
    f_x1 = func(x_1)
    f_x2 = func(x_2)
    x_3 = x_1 + 2 * delta_x if f_x1 > f_x2 else x_1 - delta_x
    f_x3 = func(x_3)


def quadratic_approximation_method(x_1, delta_x, e):
    x_2 = x_1 + delta_x
    f_x1 = func(x_1)
    f_x2 = func(x_2)
    x_3 = x_1 + 2 * delta_x if f_x1 > f_x2 else x_1 - delta_x
    f_x3 = func(x_3)

    iterator1 = 0
    f_min = min(f_x1, f_x2, f_x3)
    array = [x_1, x_2, x_3]
    x_min = 0
    for i in array:
        if func(i) == f_min:
            x_min = i
        i += 1

    x_bar = calculate_min_point(x_1, x_2, x_3, f_x1, f_x2, f_x3, delta_x)
    f_x_bar = func(x_bar)
    while abs((f_min - f_x_bar) / f_x_bar) > e:
        iterator2 = 0
        while abs((x_min - x_bar) / x_bar) > e:
            if iterator2 == 0:
                array = [x_1, x_2, x_3]
            else:
                array = [x_1, x_2, x_3, x_bar]
                remove_max_1(array)
                array.sort()
                x_1, x_2, x_3 = array
            print(f"Значение x1: {x_1}")
            print(f"Значение x2: {x_2}")
            print(f"Значение x3: {x_3}")
            f_x1 = func(x_1)
            print(f"Значение функции от x1:{f_x1}")
            f_x2 = func(x_2)
            print(f"Значение функции от x2:{f_x2}")
            f_x3 = func(x_3)
            print(f"Значение функции от x3:{f_x3}")
            f_min = min(f_x1, f_x2, f_x3)
            print(f"минимальное значение функции: {f_min}")
            for i in array:
                if func(i) == f_min:
                    x_min = i
            print(f"минимальное значение x: {x_min}")
            x_bar = calculate_min_point(x_1, x_2, x_3, f_x1, f_x2, f_x3, delta_x)

            print(f"точка минимума:{x_bar}")
            if x_bar > x_3 or x_bar < x_1:
                x_1 = x_bar
                recalculate(x_1, delta_x)
            elif x_min < x_bar:
                x_bar = x_min
            elif x_bar < x_min:
                print("Ок")
            f_x_bar = func(x_bar)
            print(f"значение точки минимума: {f_x_bar}")
            iterator2 += 1
            if iterator2 > 50:
                print("Слишком большое число итерации")
                break
        iterator1 += 1
        if iterator1 > 50:
            print("Слишком большое число итерации")
            break


def start():
    x_1 = 0.6
    delta_x = 0.2
    e = 0.0001
    quadratic_approximation_method(x_1, delta_x, e)


start()
