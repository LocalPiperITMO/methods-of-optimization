from func import InputData
import math

phi = (1 + 5**0.5) / 2


def golden_ratio(f, e, a, b, fx1, fx2, it, r, trigger, buffer):
    if it > 100:
        raise Exception
    if (b - a) < e:
        print("\nNumber of iterations: " + str(it))
        return 0.5 * (a + b)
    else:
        it += 1
        t = (b - a) / phi
        if trigger == None:
            x1, x2 = b - t, a + t
        elif trigger:
            x1, x2 = buffer, a + t
        elif not trigger:
            x1, x2 = b - t, buffer

        fx1 = fx1 if fx1 is not None else f(x1)
        fx2 = fx2 if fx2 is not None else f(x2)

        if it <= 5:
            print(
                it,
                round(a, r),
                round(b, r),
                round(x1, r),
                round(x2, r),
                round(fx1, r),
                round(fx2, r),
            )

        if fx1 >= fx2:
            return golden_ratio(f, e, x1, b, fx2, None, it, r, True, x2)
        else:
            return golden_ratio(f, e, a, x2, None, fx1, it, r, False, x1)


def perform_golden_ratio(data: InputData):
    print("\nPerforming golden ratio...")
    a = data.a
    b = data.b
    e = data.e
    f = data.f
    r = abs(int(math.log10(e))) + 1

    it = 0

    try:
        xm = golden_ratio(f, e, a, b, None, None, it, r, None, None)
        ym = f(xm)

        print("x: " + str(xm))
        print("y: " + str(ym))
    except Exception:
        print("\nMethod diverges!")
