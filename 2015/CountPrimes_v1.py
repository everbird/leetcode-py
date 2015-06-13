#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0

        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for step in range(2, int(n ** 0.5)+1):
            primes[step*step::step] = [False] * len(primes[step*step::step])

        return sum(primes)



if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(99)
    print s.countPrimes(499979)
    print s.countPrimes(2)
    print s.countPrimes(3)
    print s.countPrimes(14)
    print s.countPrimes(4)
