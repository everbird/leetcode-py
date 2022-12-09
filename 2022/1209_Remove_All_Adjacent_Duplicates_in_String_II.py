#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch, 1])
                continue

            top, tcnt = stack[-1]
            if ch == top:
                tcnt += 1
                if tcnt == k:
                    stack.pop()
                else:
                    stack[-1][1] = tcnt
            else:
                stack.append([ch, 1])

        return "".join([x[0]*x[1] for x in stack])

# Stack
