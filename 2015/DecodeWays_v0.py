#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s:
            return 0

        lens = len(s)
        d = [0] * lens
        for i in range(lens):
            if s[i] != '0':
                if i == 0:
                    d[i] = int(s[0] != '0')
                else:
                    d[i] = d[i-1]

            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                d[i] += (d[i-2] if i > 1 else 1)

        return d[-1]


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings('12')
    print s.numDecodings('123')
    print s.numDecodings('1231')
    print s.numDecodings('0')
    print s.numDecodings('10')
    print s.numDecodings('100')
    print s.numDecodings('110')
    print s.numDecodings('30')
    print s.numDecodings('310')
    print s.numDecodings('230')
    print s.numDecodings('1')
