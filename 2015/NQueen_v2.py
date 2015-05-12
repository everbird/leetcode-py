#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.result = []
        self.board = [["." for x in range(n)] for x in range(n)]
        self.n = n
        self.solve(0)
        return self.result

    def solve(self, col):
        if col == self.n:
            solution = []
            for row in self.board:
                string = ""
                for char in row:
                    string += char
                solution.append(string)
            self.result.append(solution)
            return

        for row in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = "Q"
                self.solve(col+1)
                self.board[row][col] = "."

    def isSafe(self, row, col):
        for c in range(col):
            if self.board[row][c] == "Q":
                return False
        rup = row-1
        rdown = row+1
        c = col-1
        while c >= 0:
            if rup >= 0:
                if self.board[rup][c] == "Q":
                    return False
            if rdown < self.n:
                if self.board[rdown][c] == "Q":
                    return False
            rup -= 1
            rdown += 1
            c -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    r = s.solveNQueens(8)
    print len(r)
