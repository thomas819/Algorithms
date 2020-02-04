# 1 ~ n

# me
def sum0(a):
    t = 0
    for x in range(1, a + 1):
        t += x
    return t


print(sum0(10))


def total2(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(total2(10))


def sum_n(n):
    return n * (n + 1) // 2


print(sum_n(10))


def sum2(n):
    t = 0
    for i in range(1, n + 1):
        t = t + i * i
    return t


print(sum2(10))


def sum3(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(sum3(10))
