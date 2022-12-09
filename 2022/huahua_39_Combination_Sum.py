#!/usr/bin/env python3

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rs = []

        def backtrace(items, t):
            nonlocal rs

            if t == 0:
                rs.append(items[:])
                return
            elif t < 0:
                return

            for c in candidates:
                if items and c < items[-1]:
                    continue

                items.append(c)
                backtrace(items, t-c)
                items.pop()

        backtrace([], target)

        return rs
