#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        ll = []
        for i in range(numRows):
            ll.append([])

        down_flag = True
        j = 0
        for c in s:
            ll[j].append(c)
            if down_flag:
                j += 1
            else:
                j -= 1

            if j == (numRows - 1) or j == 0:
                down_flag = not down_flag

        return ''.join([''.join(x) for x in ll])


if __name__ == '__main__':
    a = 'PAYPALISHIRING'
    n = 3
    #a = 'AB'
    #n = 1
    s = Solution()
    print s.convert(a, n)
