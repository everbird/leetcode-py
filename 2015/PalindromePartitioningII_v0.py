#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        lens = len(s)
        r = [0] * (lens + 1)
        for i in range(lens+1):
            r[i] = i - 1

        for i in range(lens):
            for j in range(i+1):
                if i+j < lens and s[i-j] == s[i+j]:
                    r[i+j+1] = min(r[i+j+1], r[i-j] + 1)
                else:
                    break

            for j in range(1, i+2):
                if i+j < lens and s[i-j+1] == s[i+j]:
                    r[i+j+1] = min(r[i+j+1], r[i-j+1] + 1)
                else:
                    break

        return r[lens]


if __name__ == '__main__':
    s = Solution()
    print s.minCut('a')
    print s.minCut('ab')
    print s.minCut('aab')
    print s.minCut('')
    print s.minCut('aabcbd')
    print s.minCut('fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi')
    print s.minCut('cabababcbc')
