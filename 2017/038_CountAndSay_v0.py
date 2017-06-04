#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        r = "1"
        for i in range(n - 1):
            r = say(r)
        return r


def say(s):
    r = ""
    while s:
        cnt = 1
        last = s[-1]
        len_s = len(s)
        while cnt < len_s and last == s[-cnt - 1]:
            cnt += 1
        r = "{}{}".format(cnt, last) + r
        s = s[:-cnt]
    return r


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)
