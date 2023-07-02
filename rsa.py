#!/usr/bin/python3
from random import randint


def ar_gcd_(i, j):
    while j:
        i, j = j, i % j
    return i


def ar_pollard_brent_(b, m, x):
    y = (x ** 2) % m + b
    if y >= m:
        y -= m

    assert 0 <= y < m
    return y


def ar_factorise_b_(n, iterations=None):
    y, c, m = (randint(1, n - 1) for w in range(3))
    r, q, g = 1, 1, 1
    i = 0
    while g == 1:
        x = y
        for w in range(r):
            y = ar_pollard_brent_(c, n, y)
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = ar_pollard_brent_(c, n, y)
                q = (q * abs(x - y)) %  n
            g = ar_gcd_(q, n)
            k += m
        r *= 2
        if iterations:
            i += 1
            if i == iterations:
                return None

    if g == n:
        while True:
            ys = ar_pollard_brent_(c, n, ys)
            g = ar_gcd_(abs(x - ys), n)
            if g > 1:
                break
    return g


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 2:
        exit(1)

    with open(argv[1], "r") as f:
        for i in f:
            n = int(i[:-1])
            res = ar_factorise_b_(n)
            print("{}={}*{}".format(n, n // res, res))
