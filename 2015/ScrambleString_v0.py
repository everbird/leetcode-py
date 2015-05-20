#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n!=m or sorted(s1) != sorted(s2):
            return False

        if s1 == s2 or n <= 3:
            return True

        for i in range(1, n):
            if (self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.isScramble('great', 'rgtae')
    print s.isScramble('great', 'rgeat')
    print s.isScramble('great', 'raegt')
    print s.isScramble('abab', 'bbaa')
