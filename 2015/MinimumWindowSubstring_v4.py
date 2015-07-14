#!/usr/bin/env python
# encoding: utf-8

import collections


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if not s or not t:
            return ''

        require = collections.Counter(t)
        p = 0
        r = ''
        count = len(t)
        for i, n in enumerate(s):
            if n in require:
                require[n] -= 1
                if require[n] >= 0:
                    count -= 1

            while count == 0:
                if not r or len(r) > (i-p+1):
                    r = s[p:i+1]

                if s[p] in require:
                    require[s[p]] += 1
                    if require[s[p]] > 0:
                        count += 1

                p += 1

        return r


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
