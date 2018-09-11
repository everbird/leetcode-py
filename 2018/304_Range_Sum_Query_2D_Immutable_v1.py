class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.len_y = len(matrix)
        self.len_x = len(matrix[0]) if matrix else 0
        def gen_dp(dx, dy):
            dp = [[0] * self.len_x for x in range(self.len_y)]
            start_x, end_x = (0, self.len_x) if dx > 0 else (-1, -(self.len_x+1))
            start_y, end_y = (0, self.len_y) if dy > 0 else (-1, -(self.len_y+1))
            dp[start_y][start_x] = matrix[start_y][start_x]
            for j in range(start_y, end_y, dy):
                for i in range(start_x, end_x, dx):
                    expand_x = -self.len_x <= (i+dx) < self.len_x
                    print expand_x, j, i, dx
                    if expand_x:
                        dp[j][i+dx] = dp[j][i] + sum(matrix[k][i+dx] for k in range(start_y, j+dy, dy))
                    expand_y = -self.len_y <= (j+dy) < self.len_y
                    if expand_y:
                        dp[j+dy][i] = dp[j][i] + sum(matrix[j+dy][k] for k in range(start_x, i+dx, dx))
                    if expand_x and expand_y:
                        dp[j+dy][i+dx] = dp[j][i+dx] + dp[j+dy][i] + matrix[j+dy][i+dx] - dp[j][i]
            return dp

        self.dp = gen_dp(1, 1) if self.len_x and self.len_y else {}


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 >= self.len_y or row2 >= self.len_y or col1 >= self.len_x or col2 >= self.len_x:
            return 0
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]

        r = self.dp[row2][col2]
        if 0 <= col1-1:
            r -= self.dp[row2][col1-1]
        if 0 <= row1-1:
            r -= self.dp[row1-1][col2]
        if 0 <= col1-1 and 0 <= row1-1:
            r += self.dp[row1-1][col1-1]
        return r



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print obj.sumRegion(2, 1, 4, 3)
    print obj.sumRegion(1, 1, 2, 2)
    print obj.sumRegion(1, 2, 2, 4)

    matrix = [
        []
    ]

    matrix = [
        [-4, -5]
    ]
    obj = NumMatrix(matrix)
    print obj.sumRegion(0, 0, 0, 0)
    print obj.sumRegion(0, 0, 0, 1)
    print obj.sumRegion(0, 1, 0, 1)
