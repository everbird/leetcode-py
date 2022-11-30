#!/usr/bin/env python3

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        def _i2xy(i):
            return i % m, i // m

        def _xy2i(x, y):
            return y*m + x

        s = 0
        e = (m * n) - 1
        while s <= e:
            mid = (s+e) // 2
            x, y = _i2xy(mid)
            midv = matrix[y][x]
            if midv == target:
                return True
            elif midv > target:
                e = mid - 1
            else:
                s = mid + 1

        return False
