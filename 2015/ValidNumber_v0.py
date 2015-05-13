#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        n = len(s)
        if n == 0:
            return False

        i = 0
        dotFlag = False
        EFlag = False
        hasDigit = False
        hasSign = False
        while i < n:
            if s[i].isdigit():
                i+=1
                hasDigit = True
                hasSign = True
            elif not dotFlag and s[i]=='.':
                i+=1
                dotFlag = True
                hasSign = True
            elif hasDigit and not EFlag and (s[i]=='e' or s[i]=='E'):
                i+=1
                dotFlag = True
                EFlag = True
                hasDigit = False
                hasSign = False
            elif not hasDigit and not hasSign and (s[i]=='+' or s[i]=='-'):
                i+=1
                hasSign = True
            else:
                return False

        if hasDigit:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print s.isNumber('0')
    print s.isNumber('0.1')
    print s.isNumber('abc')
    print s.isNumber('1 a')
    print s.isNumber('2e10')
    print s.isNumber('2ee10')
    print s.isNumber('2.')
    print s.isNumber('..2')
    print s.isNumber('0-.2')
