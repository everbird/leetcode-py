#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        lenh = len(matrix)
        lenw = len(matrix[0])
        for j in range(lenh):
            for i in range(lenw):
                matrix[j][i] = int(matrix[j][i])
                items = []
                items.append(matrix[j-1][i] if j-1 >= 0 else 0)
                items.append(matrix[j][i-1] if i-1 >= 0 else 0)
                items.append(
                    matrix[j-1][i-1]
                    if (i-1) >= 0 and (j-1) >= 0 else 0
                )

                matrix[j][i] = min(items) + 1 if matrix[j][i] == 1 else 0

        return max(map(max, matrix)) ** 2


if __name__ == '__main__':
    s = Solution()
    b = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    #b = [
        #[1, 1, 1, 0, 0],
        #[1, 0, 1, 1, 1],
        #[1, 0, 1, 0, 1],
        #[1, 1, 1, 1, 0]
    #]
    print s.maximalSquare(b)
