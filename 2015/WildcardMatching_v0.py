#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p and s:
            return False

        if not s:
            for x in p:
                if x != '*':
                    return False

            return True

        c, _p = p[0], p[1:]
        if c == '*':
            r1 = self.isMatch(s[1:], p)
            r2 = self.isMatch(s, _p)
            return r1 or r2

        elif c == '?':
            return self.isMatch(s[1:], _p)

        else:
            if c == s[0]:
                return self.isMatch(s[1:], _p)
            else:
                return False



if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aa', 'a')
    print s.isMatch('aa', 'aa')
    print s.isMatch('aaa', 'aa')
    print s.isMatch('aa', '*')
    print s.isMatch('aa', 'a*')
    print s.isMatch('aa', '?*')
    print s.isMatch('aab', 'c*a*b')
    print s.isMatch('abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab', '*aabb***aa**a******aa*')
