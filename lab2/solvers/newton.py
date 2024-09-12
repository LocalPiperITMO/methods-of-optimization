from func import InputData
import math


def perform_newton(data: InputData):
    print("\nPerforming Newton...")
    a = data.a
    b = data.b
    e = data.e
    f = data.f
    df = data.df
    d2f = data.d2f
    r = abs(int(math.log10(e))) + 1

    it = 0
    x = (a + b) / 2
    while True:
        if it > 100:
            break
        it += 1
        xi = x - df(x) / d2f(x)
        if it <= 5:
            print(
                it,
                round(x, r),
                round(xi, r),
                round(df(x), r),
                round(d2f(x), r),
                round(df(xi), r),
            )
        x = xi
        if abs(df(xi)) < e:
            break

    xm = x
    ym = f(xm)

    print("\nNumber of iterations: " + str(it))
    print("x: " + str(xm))
    print("y: " + str(ym))
