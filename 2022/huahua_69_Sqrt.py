#!/usr/bin/env python3

class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        e = x // 2 + 1
        while s <= e:
            m = (s+e) // 2
            if m*m > x and (m-1)*(m-1) <= x:
                return m-1

            if m*m <= x and (m+1)*(m+1) > x:
                return m

            if m*m > x:
                e = m - 1
            else:
                s = m + 1

        return
