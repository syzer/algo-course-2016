from gcd import gcd
from gcd_fast import gcd as gcd_fast

for i in range(1, 100):
    for j in range(1, 100):
        print('testing for ', i, j)
        assert (gcd(i, j) == gcd_fast(i, j))
