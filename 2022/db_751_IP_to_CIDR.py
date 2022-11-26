#!/usr/bin/env python3

from itertools import chain

class Solution:

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        rs = []
        s = ip2n(ip)
        e = s + n - 1
        current = s
        # Greedy
        while current < e+1:
            z = right_zeros(current)
            # When too many right zeros and n is very small, need to shrink right zeros to fit in
            while current + (2**z) > e + 1:
                z -= 1
            rs.append("{}/{}".format(n2ip(current), 32-z))    
            current += (2**z)

        return rs
        

def right_zeros(n):
    if not n:
        return 32
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n = n // 2
    return cnt


def ip2n(s):
    decimals = s.split(".")
    n = len(decimals)
    r = 0
    for i in range(n):
        m = n - i - 1
        r += int(decimals[i]) * (256 ** m)
    return r

def n2ip(n):
    decimals = []
    cnt = 4
    while cnt > 0:
        mask = 256 ** (cnt-1)
        d = n // mask
        n = n % mask
        decimals.append(d)
        cnt -= 1
    return ".".join(map(str, decimals))
