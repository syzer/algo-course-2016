from fib import fib
from fib_table import fib as fib2

for i in range(0, 1000):
    print('tesing for ',i)
    assert(fib(i) == fib2(i))