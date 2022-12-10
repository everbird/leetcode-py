#!/usr/bin/env python3

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        r = 0
        for j in range(n):
            hist = [0] * m
            for i in range(m):
                for k in range(j, n):
                    if matrix[k][i] == "1":
                        hist[i] += 1
                    else:
                        break

            r = max(r, max_hist(hist))

        return r


def max_hist(hist):
    n = len(hist)
    r = 0
    s = []
    i = 0
    while i < n:
        if not s or hist[s[-1]] <= hist[i]:
            s.append(i)
            i += 1
            continue

        _i = s.pop()
        h = hist[_i]
        w = i - (s[-1]+1) if s else i
        r = max(r, h*w)

    while s:
        i = s.pop()
        h = hist[i]
        w = n - (s[-1]+1) if s else n
        r = max(r, h*w)

    return r

# convert to Max Hist, Stack, Monotonic

# top-down hist to avoid loop with index k
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        r = 0
        g = [[0] * m for _ in range(n)]
        for j in range(n):
            for i in range(m):
                if matrix[j][i] == "1":
                    g[j][i] = g[j-1][i] + 1 if j > 0 else 1

            r = max(r, max_hist(g[j]))

        return r
