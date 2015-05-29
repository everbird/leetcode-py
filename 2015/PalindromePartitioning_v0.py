#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return [[]]

        if len(s) == 1:
            return [[s]]

        r = []
        last = s[-1]
        items = self.partition(s[:-1])
        for item in items:
            r.append(item + [last])

        for i in range(len(s)):
            substr = s[i:]
            if self.is_palindrome(substr):
                a = self.partition(s[:i])
                for j in a:
                    t = j + [substr]
                    if t not in r:
                        r.append(t)
        return r

    def is_palindrome(self, s):
        b = 0
        e = len(s)-1
        while b <= e:
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print s.partition('aa')
    print s.partition('aab')
    print s.partition('aabcbd')
