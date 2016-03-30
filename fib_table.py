# Uses python3
table = [0, 1, 1]


def fib(n):
    if n <= 2:
        return table[n]

    for i in range(3, n + 1):
        table.append((table[i - 1] + table[i - 2]))

    return table[n]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
