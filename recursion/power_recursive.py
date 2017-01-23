def isEven(num):
    return num % 2 == 0


# a^b = a*a * a^(b/2)
# so it halves calc every time compored to naive approach
# O(log b)
def pow(base, exponent):
    if exponent == 0:
        return 1
    elif isEven(exponent):
        return pow(base * base, exponent / 2)
    else:
        return base * pow(base * base, (exponent - 1) / 2)


print(pow(3, 4))
# 81