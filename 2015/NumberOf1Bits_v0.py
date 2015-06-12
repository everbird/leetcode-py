#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return len([i for i in range(32) if (1<<i)&n])

    def _hammingWeight(self, n):
        cnt = 0
        for i in range(32):
            if (1 << i) & n:
                cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(11)
