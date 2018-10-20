# Uses python3

def fib_t(n):
    table = [0, 1, 1]

    if n <= 2:
        return table[n]

    for i in range(3, n + 1):
        table.append((table[i - 1] + table[i - 2]))

    return table[n]


if __name__ == '__main__':
    n = int(input())
    print(fib_t(n))
