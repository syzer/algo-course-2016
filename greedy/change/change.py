# Uses python3
import sys


def get_change(n):
    coins = 0

    while (n >= 10) and (n // 10):
        n -= 10
        coins += 1

    while (n >= 5) and (n // 5):
        n -= 5
        coins += 1

    return coins + n


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
