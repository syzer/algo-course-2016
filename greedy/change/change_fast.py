# Uses python3
import sys


def get_change(n):
    coins = 0

    if (n >= 10) and (n // 10):
        coins += n // 10
        n -= 10 * (n // 10)

    if (n >= 5) and (n // 5):
        coins += n // 5
        n -= 5 * (n // 5)

    return coins + n


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
