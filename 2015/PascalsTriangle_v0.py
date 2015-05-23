#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if not numRows:
            return []

        li = [1]
        r = [li[:]]
        for i in range(numRows-1):
            li.append(0)
            new = [1]
            for j in range(len(li)-1):
                new.append(sum(li[j:j+2]))

            r.append(new[:])
            li = new

        return r


if __name__ == '__main__':
    s = Solution()
    print s.generate(5)
    print s.generate(1)
    print s.generate(0)
