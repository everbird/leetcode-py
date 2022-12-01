#!/usr/bin/env python3

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        e = n - 1
        w = 0
        pre = None

        for i in range(n):
            if pre is None:
                pre = i
                continue

            if height[i] >= height[pre]:
                w += height[pre]*(i-pre) - sum(height[pre:i])
                pre = i

        left_end = pre

        pre = None
        for i in range(n-1, left_end-1, -1):
            if pre is None:
                pre = i
                continue

            if height[i] >= height[pre]:
                w += height[pre]*(pre-i) - sum(height[i+1:pre+1])
                pre = i

        return w
