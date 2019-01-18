def recur_karatsuba(x, y):
    if x < 10 or y < 10:
        print(x, y)
        return x*y
    m = max(len(str(x)), len(str(y)))
    if m % 2 == 0:  # Is it even?
        m = m // 2
    else:
        m = (m + 1) // 2
    p = 10**m

    a, b = x // p, x % p
    c, d = y // p, y % p

    z0 = recur_karatsuba(b, d)
    z2 = recur_karatsuba(a, c)
    z1 = recur_karatsuba(a, d) + recur_karatsuba(b, c)
    print(z0, z2, z1)
    return z0 + (z2 * 10 ** (m * 2)) + (z1 * p)
