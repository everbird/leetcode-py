#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} digits
    # @return {string[]}



    def letterCombinations(self, digits):
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if not digits:
            return []

        if len(digits) == 1:
            return d.get(digits)

        ret = []
        char = digits[0]
        chars = d.get(char)
        rs = self.letterCombinations(digits[1:])
        for r in rs:
            for c in chars:
                ret.append(c + r)
        return ret


if __name__ == '__main__':
    digits = '23'
    s = Solution()
    r = s.letterCombinations(digits)
    print r
