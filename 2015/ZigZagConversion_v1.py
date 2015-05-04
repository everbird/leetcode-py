#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = []
        for i in range(numRows):
            rows.append([])

        f_int = -1
        n = 0
        for i, c in enumerate(s):
            row = rows[n]
            row.append(c)
            if n == numRows - 1 or n == 0:
                f_int = -f_int

            n += f_int

        return ''.join([''.join(x) for x in rows])


if __name__ == '__main__':
    #a = 'PAYPALISHIRING'
    #n = 3
    a = 'AB'
    n = 1
    s = Solution()
    print s.convert(a, n)
