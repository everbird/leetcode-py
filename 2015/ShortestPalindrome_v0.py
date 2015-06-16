#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        lens = len(s)
        index = -1
        for i in range(lens-1, -1, -1):
            _s = s[:i+1]
            if self.is_panlindrome(_s):
                index = i
                break

        rest = s[index+1:]
        return rest[::-1]+s

    def is_panlindrome(self, s):
        lens = len(s)
        b = 0
        e = lens - 1
        while b <= e:
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print s.shortestPalindrome('aacecaaa')
    print s.shortestPalindrome('abcd')
