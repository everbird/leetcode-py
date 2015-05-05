#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} digits
    # @return {string[]}

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

    def letterCombinations(self, digits):
        if not digits:
            return []

        return reduce(
            lambda acc, digit: [x + y for x in acc for y in self.d[digit]],
            digits,
            ['']
        )


if __name__ == '__main__':
    digits = '23'
    s = Solution()
    r = s.letterCombinations(digits)
    print r
