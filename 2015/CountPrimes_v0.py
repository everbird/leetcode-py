#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        cnt = 0
        for i in range(1, n+1):
            if self.is_prime(i):
                cnt += 1

        return cnt

    def is_prime(self, n):
        for i in range(2, n):
            if (n % i) == 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(99)
