memo = {0: 1, 1: 1}


def fib(n):
    if n <= 1:
        return 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
