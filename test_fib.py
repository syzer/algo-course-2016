from fib import fib
from fib_table import fib_t

for i in range(0, 1001000):
    print('testing for ', i)
    assert (fib(i) == fib_t(i))
