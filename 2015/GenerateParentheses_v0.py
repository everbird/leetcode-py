#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []

        if n == 1:
            return ['()', ]

        return get_p('', nl=n, nr=n)


def get_p(s, nl, nr):
    if nl == 0 and nr > 0:
        return [s + ')' * nr]

    r = []
    if 0 < nl < nr:  # nr should always equal or geater than nl
        r += get_p(s+'(', nl - 1, nr)
        r += get_p(s+')', nl, nr - 1)
    elif nl == nr and nl != 0: # when nl == nr, should only append ( at most right side
        r += get_p(s+'(', nl - 1, nr)
    return r


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print r

    r = s.generateParenthesis(4)
    print r
