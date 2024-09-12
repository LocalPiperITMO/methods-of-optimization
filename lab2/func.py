import math
from dataclasses import dataclass

default_a = 0.5
default_b = 1.5
default_e = 0.001
default_f = lambda x: 1 / x + math.pow(math.e, x)
default_df = lambda x: -1 / math.pow(x, 2) + math.pow(math.e, x)


@dataclass
class InputData:

    def __init__(self, a, b, e, f, df, d2f):
        self.a = a
        self.b = b
        self.e = e
        self.f = f
        self.df = df
        self.d2f = d2f

    def __post_init__(self):
        print("Performing health checks...")

        if self.a == None:
            print("Invalid a value, switching to default...")
            self.a = default_a
        if self.b == None:
            print("Invalid b value, switching to default...")
            self.b = default_b
        if self.a > self.b:
            print('Condition "a < b" unsatisfied: swapping...')
            self.a, self.b = self.b, self.a
        if self.e == None:
            print("Invalid presicion value, switching to default...")
            self.e = default_e
        else:
            if (self.a < 0) or (self.a >= 1):
                print("Invalid presicion value, switching to default...")
                self.e = default_e
        if self.f == None:
            print("Invalid function, switching to default...")
            self.f = default_f
            self.df = default_df
        if self.df == None:
            print("Invalid derivative, switching to default...")
            self.f = default_f
            self.df = default_f

        print("Health checks complete")
