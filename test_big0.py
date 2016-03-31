import math

n = 200


def first(n):
    return pow(3, n)


def second(n):
    return n * math.log(n, 2)


def forth(n):
    return n


def third(n):
    return math.log(n, 4)


def five(n):
    return pow(n, 2.31)


def six(n):
    return pow(n, 2)


def seven(n):
    return pow(n, 0.5)


def eigth(n):
    return pow(4, n)


print("3,%d" % third(n))
print("%d" % seven(n))
print("%d" % forth(n))
print("%d" % second(n))
print("%d" % six(n))
print("5,%d" % five(n))
print("1,%d" % first(n))
print("8,%d" % eigth(n))
