#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if not s1:
            return s2 == s3

        if not s2:
            return s1 == s3

        c1 = s1[0]
        c2 = s2[0]
        c3 = s3[0]
        if c3 == c2 and c3 == c1:
            return self.isInterleave(s1, s2[1:], s3[1:]) \
                or self.isInterleave(s1[1:], s2, s3[1:])
        elif c3 == c2:
            return self.isInterleave(s1, s2[1:], s3[1:])
        elif c3 == c1:
            return self.isInterleave(s1[1:], s2, s3[1:])

        return False


if __name__ == '__main__':
    s = Solution()
    print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
