#!/usr/bin/env python
# encoding: utf-8


cache_store = {}


def cache(f):
    def _(inst, n):
        v = cache_store.get(n)
        if v is None:
            v = f(inst, n)
            cache_store[n] = v
        return v
    return _


class Solution:
    # @param {integer} n
    # @return {integer}
    @cache
    def numTrees(self, n):
        if n == 0:
            return 0

        if n == 2:
            return 2

        if n == 1:
            return 1

        c = 0
        for i in range(0, n):
            lc = self.numTrees(i)
            rc = self.numTrees(n - i - 1)
            t = 0
            if lc == 0:
                t = rc
            elif rc == 0:
                t = lc
            else:
                t = lc * rc
            c += t

        return c


if __name__ == '__main__':
    s = Solution()
    print s.numTrees(3)
    print s.numTrees(19)
