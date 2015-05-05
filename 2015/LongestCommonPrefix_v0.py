#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        i = 0
        prefix = ''
        first_str = strs[0]
        lenf = len(first_str)
        same = True
        while same:
            for s in strs:
                same &= ((i <= (len(s) - 1)) and (i <= (lenf - 1)) and s[i] == first_str[i])

            if same:
                prefix += first_str[i]

            i += 1

        return prefix


if __name__ == '__main__':
    a = [
        'abcdefg',
        'abcdlhe',
        'abc',
    ]
    #a = ["","cbb",""]
    s = Solution()
    r = s.longestCommonPrefix(a)
    print r
