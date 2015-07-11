#!/usr/bin/env python
# encoding: utf-8


def pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x

    v = pow(x, n // 2)
    r = v*v
    if n % 2:
        r *= x
    return r

if __name__ == '__main__':
    print pow(2, 10)
    print pow(3, 3)
