def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    gcd_a_b = gcd(a, b)
    res = (a * b) // gcd_a_b

    return res




a = 12
b = 15


print(gcd(a, b))
print(lcm(a, b))
