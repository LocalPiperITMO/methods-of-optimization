def perform_halving_division(f, x, y):
    a = -1000
    b = 1000
    e = 0.01
    f = f

    try:
        it = 0
        while True:
            if it > 100:
                raise Exception
            it += 1
            x1 = (a + b - e) / 2
            x2 = (a + b + e) / 2

            y1 = f(x, y, x1)
            y2 = f(x, y, x2)

            if y1 > y2:
                a = x1
            else:
                b = x2

            if (b - a) <= (2 * e):
                break

        xm = (a + b) / 2

        return xm
    except Exception:
        print("\nMethod diverges!")
