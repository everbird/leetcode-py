#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} digits
    # @return {string[]}

    d = {
        1: [],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
        0: [],
    }

    def letterCombinations(self, digits):
        if not digits:
            return []

        if len(digits) == 1:
            return self.d[ord(digits[0]) - ord('0')]

        cs = self.letterCombinations(digits[:-1])
        r = []
        for cc in cs:
            for char in self.d[ord(digits[-1]) - ord('0')]:
                r.append(cc + char)
        return r


if __name__ == '__main__':
    digits = '23'
    s = Solution()
    r = s.letterCombinations(digits)
    print r
