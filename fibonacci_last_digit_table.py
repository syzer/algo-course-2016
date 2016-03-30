# Uses python3
memo = {1: 1, 2: 1}


def last_num_table(n):
    if n <= 2:
        return 1

    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 10

    return memo[n]


if __name__ == '__main__':
    n = int(input())
    print(last_num_table(n))
