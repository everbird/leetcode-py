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

        for i in self.finds(s[:-1], last):
            if self.is_palindrome(s[i+1:-1]):
                a = self.partition(s[:i])
                for j in a:
                    t = j + [s[i:]]
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

    def finds(self, s, c):
        for i in range(len(s)):
            if s[i] == c:
                yield i


if __name__ == '__main__':
    s = Solution()
    print s.partition('aa')
    print s.partition('aab')
    print s.partition('aabcbd')
    print s.partition('amanaplanacanalpanama')
