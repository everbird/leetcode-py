#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        return get_p('(', 1, 0, n)


def get_p(prefix, left, right, n):
    if n == 0:
        return []

    if left == n:
        return [prefix + ')' * (n - right)]
    elif right == left:
        return get_p(prefix+'(', left + 1, right, n)
    elif right < left < n:
        return get_p(prefix+'(', left + 1, right, n) + get_p(prefix+')', left, right + 1, n)

    return []



if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print r

    r = s.generateParenthesis(4)
    print r
