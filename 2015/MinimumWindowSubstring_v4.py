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
        cmap = {x: True for x in t}
        p = 0
        min_l = 2**31
        rb = -1
        count = len(t)
        for i, n in enumerate(s):
            require[n] -= 1
            if cmap.get(n) and require[n] >= 0:
                count -= 1

            while count == 0:
                if min_l > (i - p + 1):
                    min_l = i - p + 1
                    rb = p
                require[s[p]] += 1
                if cmap.get(s[p]) and require[s[p]] > 0:
                    count += 1

                p += 1

        return s[rb:rb+min_l] if min_l != 2**31 else ''


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
