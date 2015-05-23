#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        r = [1]
        for i in range(rowIndex):
            new = [1]
            r.append(0)
            for j in range(len(r)-1):
                new.append(sum(r[j:j+2]))

            r = new

        return r


if __name__ == '__main__':
    s = Solution()
    print s.getRow(5)
    print s.getRow(3)
    print s.getRow(1)
    print s.getRow(0)
