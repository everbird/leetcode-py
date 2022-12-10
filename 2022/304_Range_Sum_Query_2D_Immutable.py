#!/usr/bin/env python3

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.lsum = [[0] * m for _ in range(n)]

        for j in range(n):
            for i in range(m):
                v = matrix[j][i]
                if i == 0 and j == 0:
                    self.lsum[0][0] = v
                elif i == 0:
                    self.lsum[j][0] = self.lsum[j-1][0] + v
                elif j == 0:
                    self.lsum[0][i] = self.lsum[0][i-1] + v
                else:
                    self.lsum[j][i] = self.lsum[j-1][i] + self.lsum[j][i-1] + v - self.lsum[j-1][i-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r = self.lsum[row2][col2]
        if col1 != 0:
            r -= self.lsum[row2][col1-1]

        if row1 != 0:
            r -= self.lsum[row1-1][col2]

        if row1 != 0 and col1 != 0:
            r += self.lsum[row1-1][col1-1]

        return r

# math, lsum
