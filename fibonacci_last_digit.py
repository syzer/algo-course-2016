# Uses python3
# import sys

memo = {}


def fib(n):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = (fib(n - 1) + fib(n - 2)) % 10
    return memo[n]


def get_fibonacci_last_digit(n):
    return fib(n)


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
