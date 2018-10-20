# Uses python3

def last_num_table(n):
    memo = [0, 1, 1]

    if n <= 2:
        return memo[n]

    for i in range(3, n + 1):
        memo.append((memo[i - 1] + memo[i - 2]) % 10)

    return memo[n]


if __name__ == '__main__':
    n = int(input())
    print(last_num_table(n))
