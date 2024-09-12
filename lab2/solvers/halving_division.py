from func import InputData
import math


def perform_halving_division(data: InputData):
    print("\nPerforming halving division...")
    a = data.a
    b = data.b
    e = data.e
    f = data.f
    r = abs(int(math.log10(e))) + 1

    try:
        it = 0
        while True:
            if it > 100:
                raise Exception
            it += 1
            x1 = (a + b - e) / 2
            x2 = (a + b + e) / 2

            y1 = f(x1)
            y2 = f(x2)
            if it <= 5:
                print(it, round(x1, r), round(x2, r), round(y1, r), round(y2, r))

            if y1 > y2:
                a = x1
            else:
                b = x2

            if (b - a) <= (2 * e):
                break

        xm = (a + b) / 2
        ym = f(xm)

        print("\nNumber of iterations: " + str(it))
        print("x: " + str(xm))
        print("y: " + str(ym))
    except Exception:
        print("\nMethod diverges!")
