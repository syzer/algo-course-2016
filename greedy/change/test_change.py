from change import get_change
from change_fast import get_change as get_change_fast

print('finaly', get_change(26))

for i in range(0, 1000):
    print('testing', i)
    assert (get_change(i) == get_change_fast(i))
