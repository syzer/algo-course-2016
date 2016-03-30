from fib import fib
from fib_table import fib as fib2

for i in range(0, 10):
    print('tesing for ',i, fib(i), fib2(i))
    assert(fib(i), fib2(i))