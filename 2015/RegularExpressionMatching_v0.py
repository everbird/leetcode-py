#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        lenp = len(p)
        lens = len(s)
        si = lens - 1
        actions = []
        n = lenp - 1
        tmp = ''
        while n >= 0:
            if p[n] == '*':
                if tmp:
                    actions.append((tmp, None))

                actions.append((p[n - 1], '*'))
                tmp = ''
                n -= 1
            else:
                tmp += p[n]

            n -= 1

        if tmp:
            actions.append((tmp, None))

        pre_consumed = ''
        for ps, opt in actions:
            if not opt:
                pos = pre_consumed.rfind(ps[::-1])
                if pos != -1:
                    si += pos + len(ps)

                print 'pos:', pos, len(ps), si
                for c in ps:
                    if si < 0 or not (s[si] == c or c == '.'):
                        return False
                    si -= 1
            else:
                b = si
                while si >= 0 and (s[si] == ps or ps == '.'):
                    si -= 1
                if b != si:
                    pre_consumed = s[si + 1:b + 1]

        return si == -1


if __name__ == '__main__':
    s = Solution()
    #print s.isMatch('aa', 'a')
    #print s.isMatch('aa', 'aa')
    #print s.isMatch('aaa', 'aa')
    #print s.isMatch('aa', 'a*')
    #print s.isMatch('aa', '.*')
    #print s.isMatch('ab', '.*')
    #print s.isMatch('aab', 'c*a*b')
    #print s.isMatch('aaa', 'a.a')
    #print s.isMatch('aaa', 'a*a')
    print s.isMatch('aaa', 'ab*a*c*a')
    #print s.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s')
