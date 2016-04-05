# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1

    while n > 2 * i:
        n = n - i
        summands.append(i)
        i += 1

    if n:
        summands.append(n)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
