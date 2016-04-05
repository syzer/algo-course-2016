# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1
    sum = 0

    while (sum * 2 + 2) < n:
        summands.append(i)
        sum += i
        i += 1

    summands.append(n - sum)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
