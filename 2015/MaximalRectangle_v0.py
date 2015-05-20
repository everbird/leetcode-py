#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        lenh = len(matrix)
        lenw = len(matrix[0])
        h = []
        for j in range(lenh):
            counts = []
            for i in range(lenw):
                count = 0
                if matrix[j][i] == "1":
                    count = 1
                    t = j + 1
                    while t < lenh and matrix[t][i] == "1":
                        count += 1
                        t += 1

                counts.append(count)

            h.append(counts)

        max_a = 0
        for row in h:
            max_a = max(max_a, self.largestRectangleArea(row))

        return max_a

    def largestRectangleArea(self, height):
        i = 0
        max_a = 0
        s = []
        h = height[:]
        h.append(0)
        while i < len(h):
            if not s or h[i] >= h[s[-1]]:
                s.append(i)
                i += 1
            else:
                t = s.pop()
                v = (i-1) - (s[-1] + 1) + 1 if s else i
                max_a = max(max_a, h[t]*v)

        return max_a


if __name__ == '__main__':
    s = Solution()
    #print s.maximalRectangle([
        #[0,1,1,0,0],
        #[0,1,1,1,0],
        #[0,1,1,0,0],
        #[0,0,1,0,0],
        #[1,0,0,0,1],
    #])
    print s.maximalRectangle([
        "01100",
        "01110",
        "01100",
        "00100",
        "10001",
    ])

    print s.maximalRectangle(["1"])
