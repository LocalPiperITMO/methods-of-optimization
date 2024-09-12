import math
from func import InputData
from solvers.halving_division import perform_halving_division
from solvers.golden_ratio import perform_golden_ratio
from solvers.chord import perform_chord
from solvers.newton import perform_newton

if __name__ == "__main__":
    data = InputData(
        a=0.5,
        b=1.5,
        e=0.001,
        f=lambda x: 1 / x + math.pow(math.e, x),
        df=lambda x: -1 / math.pow(x, 2) + math.pow(math.e, x),
        d2f=lambda x: 2 / math.pow(x, 3) + math.pow(math.e, x),
    )

    perform_halving_division(data)
    perform_golden_ratio(data)
    perform_chord(data)
    perform_newton(data)
