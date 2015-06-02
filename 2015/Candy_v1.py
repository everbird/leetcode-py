#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        lenn = len(ratings)
        r = [1] * lenn
        for i in range(lenn-1):
            a = ratings[i]
            b = ratings[i+1]
            if a < b:
                r[i+1] = r[i] + 1

        for i in range(lenn-1, 0, -1):
            a = ratings[i-1]
            b = ratings[i]
            if a > b:
                r[i-1] = max(r[i-1], r[i]+1)

        return sum(r)


if __name__ == '__main__':
    s = Solution()
    print s.candy([1,2,3,4])
    print s.candy([1,2,3,4,4])
    print s.candy([2,4,1])
