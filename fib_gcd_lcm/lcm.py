# Uses python3

def lcm(a, b):
    return a * b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
