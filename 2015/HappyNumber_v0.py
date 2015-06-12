#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        visited = []
        return self._is_happy(n, visited)

    def _is_happy(self, n, visited):
        if n in visited:
            return False

        r = 0
        visited.append(n)
        while n:
            v = n % 10
            r += v*v
            n = n / 10

        if r==1:
            return True

        return self._is_happy(r, visited)


if __name__ == '__main__':
    s = Solution()
    print s.isHappy(19)
    print s.isHappy(20)
