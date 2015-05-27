#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.lower().strip()
        b = 0
        e = len(s) - 1
        while b <= e:
            while b <= (len(s) - 1) and s[b] not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                b += 1

            while e >= 0 and s[e] not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                e -= 1

            if b > e:
                break

            if s[b] != s[e]:
                return False

            b += 1
            e -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('A man, a plan, a canal: Panama')
    print s.isPalindrome('race a car')
    print s.isPalindrome('')
    print s.isPalindrome(' ')
    print s.isPalindrome('.')
