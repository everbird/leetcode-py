#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        lens = len(s)
        e = lens - 1
        while e >= 0 and s[e] == ' ':
            e -= 1

        count = 0
        for i in range(e, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                return count

        return count


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord('Hello World')
    print s.lengthOfLastWord('HelloWorld')
    print s.lengthOfLastWord('  ')
    print s.lengthOfLastWord('')
    print s.lengthOfLastWord('a ')
    print s.lengthOfLastWord('b a ')
