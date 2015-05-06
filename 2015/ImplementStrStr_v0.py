#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i:i + n]:
                return i

        return -1


if __name__ == '__main__':
    h = 'akfdsadfhklh'
    n = 'dsad'
    s = Solution()
    r = s.strStr(h, n)
    print r
