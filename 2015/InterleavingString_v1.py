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

        len1 = len(s1)
        len2 = len(s2)

        if (len1 + len2) != len(s3):
            return False

        li = [0] * (len1+1)
        d = [li[:] for i in range(len2+1)]

        for j in range(len2+1):
            for i in range(len1+1):
                if i == 0 and j == 0:
                    d[j][i] = 1
                elif i == 0:
                    d[j][i] = int(s3[:i+j] == s2[:j])
                elif j == 0:
                    d[j][i] = int(s3[:i+j] == s1[:i])
                else:
                    d[j][i] = int((s3[i+j-1] == s1[i-1] and d[j][i-1] == 1)
                                  or (s3[i+j-1] == s2[j-1] and d[j-1][i] == 1))

        return bool(d[-1][-1])


def printm(d):
    for li in d:
        print li



if __name__ == '__main__':
    s = Solution()
    #print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    #print s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
    print s.isInterleave('a', 'b', 'a')
