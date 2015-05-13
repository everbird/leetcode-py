#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        for i in range(m):
            if obstacleGrid[i][0] == -1:
                break
            else:
                obstacleGrid[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == -1:
                break
            else:
                obstacleGrid[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == -1:
                    continue
                obstacleGrid[i][j] = max(obstacleGrid[i - 1][j], 0) + max(obstacleGrid[i][j - 1], 0)

        return obstacleGrid[m - 1][n - 1] if obstacleGrid[m - 1][n - 1] != -1 else 0


if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsWithObstacles([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ])

    print s.uniquePathsWithObstacles([
        [1],
    ])
