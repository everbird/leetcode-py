#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        i = 0
        if not len(strs):
            return ''

        min_l = min(map(len, strs))
        first_s = strs[0]
        while i < min_l:
            c = first_s[i]
            if not all(c == s[i] for s in strs):
                break
            i += 1
        return first_s[:i]



if __name__ == '__main__':
    a = [
        'abcdefg',
        'abcdlhe',
        'abc',
    ]
    #a = ["","cbb",""]
    #a = ['a', 'b']
    s = Solution()
    r = s.longestCommonPrefix(a)
    print r
