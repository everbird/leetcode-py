#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        min_l = min(map(len, strs))
        i = 0
        while (i < min_l) and all_same(map(lambda x: x[i], strs)):
            i += 1

        return strs[0][:i] if i > 0 else ''


def all_same(array):
    for i in range(len(array) - 1):
        if array[i] != array[i + 1]:
            return False

    return True


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
