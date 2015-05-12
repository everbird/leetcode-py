#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        s = range(1, n+1)

        while k - 1:
            peek = n - 1
            for i in range(n-1, 0, -1):
                if s[i] > s[i-1]:
                    peek = i
                    break

            right = s[peek+1:]
            if not right:
                s[peek], s[peek - 1] = s[peek - 1], s[peek]

            else:
                x = s[peek - 1]
                for i in range(peek+1, n+1):
                    if i == n or s[i] < x:
                        s[peek - 1], s[i-1] = s[i-1], s[peek - 1]
                        break

                _r = sorted(s[peek:])
                s = s[:peek] + _r

            k -= 1

        return s


if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(9, 273815)
