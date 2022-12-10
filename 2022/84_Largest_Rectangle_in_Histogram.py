#!/usr/bin/env python3

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        n = len(heights)
        r = 0
        i = 0
        while i < n:
            if not s:
                s.append(i)
                i += 1
                continue

            if heights[i] >= heights[s[-1]]:
                s.append(i)
                i += 1
                continue

            _i = s.pop()
            width = i - s[-1] - 1 if s else i
            height = heights[_i]
            r = max(r, width*height)

        while s:
            i = s.pop()
            width = n - s[-1] - 1 if s else n
            height = heights[i]
            r = max(r, width*height)

        return r

# Stack, deal with non-acs left portion. At last deal with the acs portion

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [-1]
        n = len(heights)
        r = 0
        for i in range(n):
            while s[-1] != -1 and heights[s[-1]] >= heights[i]:
                _i = s.pop()
                current_height = heights[_i]
                current_width = i - s[-1] - 1  # s[-1]+1 is the left of this rect
                r = max(r, current_height*current_width)

            s.append(i)

        while s[-1] != -1:
            i = s.pop()
            current_height = heights[i]
            current_width = n - s[-1] - 1
            r = max(r, current_height*current_width)

        return r
