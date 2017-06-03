#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p and not s:
            return True
        elif not p:
            return False


        len_p = len(p)
        if len_p == 1:
            if p == '.' and len(s) == 1:
                return True
            return s == p

        c = p[0]
        opt = p[1]
        if opt == '*':
            if s and (s[0] == c or c == '.'):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        else:
            if s and (s[0] == c or c == '.'):
                return self.isMatch(s[1:], p[1:])
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
    print s.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')
