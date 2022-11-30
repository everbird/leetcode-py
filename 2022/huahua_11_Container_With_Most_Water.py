#!/usr/bin/env python3

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        e = n-1
        r = 0
        while s < e:
            hs = height[s]
            he = height[e]
            h = min(hs, he)
            w = e - s
            r = max(r, h*w)

            if hs < he:
                s += 1
            else:
                e -= 1

        return r
