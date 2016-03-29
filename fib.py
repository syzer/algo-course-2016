n = int(input())

memo = {}


def fib(n):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n - 1] = fib(n - 1)
    memo[n - 2] = fib(n - 2)

    return memo[n - 1] + memo[n - 2]


print(fib(n))
