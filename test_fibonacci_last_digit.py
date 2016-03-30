from fibonacci_last_digit import get_fibonacci_last_digit as last_digit
from fibonacci_last_digit_table import last_num_table

for i in range(0, 1000):
    print('testing for ', i)
    assert (last_digit(i) == last_num_table(i))

assert (last_num_table(327305) == 5)
