# Uses python3
import sys

memo = {}


def fib(n):
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n - 2] = fib(n - 2) % 10
    memo[n - 1] = fib(n - 1) % 10
    memo[n] =  (memo[n - 2] + memo[n - 1]) % 10
    return memo[n]


def get_fibonacci_last_digit(n):
    sys.setrecursionlimit(100000)
    return fib(n)


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
