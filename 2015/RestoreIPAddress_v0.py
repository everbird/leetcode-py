#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        return self.split(s, 4)

    def split(self, s, count):
        if not s:
            return []

        if count == 1:
            return [s] \
                if (s == '0' or not s.startswith('0')) and 0 <= int(s) <= 255 \
                else []

        r = []
        s1 = s[0]
        items1 = self.split(s[1:], count - 1)
        for i in items1:
            r.append(s1+'.'+i)

        s2 = s[:2]
        if not s2.startswith('0'):
            items2 = self.split(s[2:], count - 1)
            for i in items2:
                r.append(s2+'.'+i)

        s3 = s[:3]
        if not s3.startswith('0') and int(s3) <= 255:
            items3 = self.split(s[3:], count - 1)
            for i in items3:
                r.append(s3+'.'+i)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.restoreIpAddresses('25525511135')
    print s.restoreIpAddresses('0000')
    print s.restoreIpAddresses('010010')
