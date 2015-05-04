#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s and not p:
            return True

        if not p and s:
            return False

        if p[-1] == '*':
            rep = p[-2]
            if s and (s[-1] == rep or rep == '.'):
                return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (p[-1] == s[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aa', 'a')
    print s.isMatch('aa', 'aa')
    print s.isMatch('aaa', 'aa')
    print s.isMatch('aa', 'a*')
    print s.isMatch('aa', '.*')
    print s.isMatch('ab', '.*')
    print s.isMatch('aab', 'c*a*b')
    print s.isMatch('aaa', 'a.a')
    print s.isMatch('aaa', 'a*a')
    print s.isMatch('aaa', 'ab*a*c*a')
    print s.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s')
    print s.isMatch('a', '.*..a*')
