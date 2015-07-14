#!/usr/bin/env python
# encoding: utf-8

import collections


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        sett = set(t)
        require = collections.Counter(t)
        b, e = -1, -1
        lens = len(s)
        min_win = ''
        while e < lens:
            if b != -1 and s[b] in sett:
                require[s[b]] += 1
            b += 1
            while b < e and s[b] not in sett:
                # move left
                b += 1

            while not self.is_valid(require):
                # move right
                e += 1
                if e >= lens:
                    break

                if s[e] in sett:
                    require[s[e]] -= 1

            # verify
            if self.is_valid(require):
                if not min_win or len(min_win) > (e-b+1):
                    min_win = s[b:e+1]

        return min_win

    def is_valid(self, require):
        return all(v <= 0 for v in require.values())


if __name__ == '__main__':
    s = Solution()
    print s.minWindow('ADOBECODEBANC', 'ABC')
    print s.minWindow('ADOBECODEBANC', 'ABCZ')
    print s.minWindow('a', 'a')
    print s.minWindow('a', 'b')
    print s.minWindow('ab', 'A')
    print s.minWindow('ab', 'b')
    print s.minWindow('aa', 'aa')
    print s.minWindow("onlswwtraopuasovmrmdouldsqiryidoxpgtlcmnschswxpirbmfxzkqpsjncnebekupoheglmyhlqsctgirfsjunskrfotj", "apapyfvjtwtemnhf")
