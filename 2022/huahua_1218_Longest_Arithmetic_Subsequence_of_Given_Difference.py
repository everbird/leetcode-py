#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        r = 0
        for n in arr:
            if d[n-difference]:
                d[n] = d[n-difference] + 1
            else:
                d[n] = 1

            r = max(r, d[n])

        return r
