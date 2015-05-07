#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        r = '1'
        for i in range(n - 1):
            r = say(r)

        return str(r)


def say(n):
    r = ''
    p = -1
    count = 0
    for c in n:
        if p != c:
            if p != -1:
                r += str(count) + p
            count = 1
        else:
            count += 1

        p = c

    return r + str(count) + p


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)
    print say('11')
    print say('21')
