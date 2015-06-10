#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    s = Solution()
    print s.reverseWords('the sky is blue')
    print s.reverseWords('  ')
