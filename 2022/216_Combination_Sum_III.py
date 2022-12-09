#!/usr/bin/env python3

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        rs = []

        def backtrack(cnt, items):
            if cnt == 0 and sum(items) == n:
                rs.append(items[:])
                return
            elif cnt < 0:
                return

            for i in range(1, 10):
                if items and items[-1] >= i:
                    continue

                items.append(i)
                backtrack(cnt-1, items)
                items.pop()

        backtrack(k, [])
        return rs
