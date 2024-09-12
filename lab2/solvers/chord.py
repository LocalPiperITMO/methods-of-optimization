from func import InputData
import math


def perform_chord(data: InputData):
    print("\nPerforming chord...")
    a = data.a
    b = data.b
    e = data.e
    f = data.f
    df = data.df
    r = abs(int(math.log10(e))) + 1

    try:
        it = 0
        while True:
            if it > 100:
                raise Exception
            it += 1
            x = a - df(a) * (a - b) / (df(a) - df(b))
            if it <= 5:
                print(
                    it,
                    round(a, r),
                    round(b, r),
                    round(df(a), r),
                    round(df(b), r),
                    round(x, r),
                    round(df(x), r),
                )
            if abs(df(x)) <= e:
                xm = x
                ym = f(xm)

                print("\nNumber of iterations: " + str(it))
                print("x: " + str(xm))
                print("y: " + str(ym))
                break

            if df(x) > 0:
                b = x
            else:
                a = x
    except Exception:
        print("\nMethod diverges!")
