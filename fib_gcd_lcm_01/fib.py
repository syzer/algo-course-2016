memo = {}


def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n - 1] = fib(n - 1)
    memo[n - 2] = fib(n - 2)

    return memo[n - 1] + memo[n - 2]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
