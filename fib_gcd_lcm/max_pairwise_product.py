# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
assert (len(a) == n)

print(a[0] * a[1])
