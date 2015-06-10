#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        e = b = 0
        lens = len(s)
        for i in range(lens):
            n = s[i]
            if n == ' ':
                e = i - 1
                s = self.reverse(s, b, e)
                b = i+1

        if b < lens:
            return self.reverse(s, b, lens-1)

        return s

    def reverse(self, s, b, e):
        return s[:b]+s[e:b-1 if b > 0 else None:-1]+s[e+1:]


if __name__ == '__main__':
    s = Solution()
    print s.reverseWords('the sky is blue')
    print s.reverseWords('  ')
