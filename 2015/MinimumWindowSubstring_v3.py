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
        found = collections.defaultdict(int)
        p = 0
        min_l = 2**31
        rb = re = -1
        for i, n in enumerate(s):
            found[n] += 1
            while self.is_valid_window(require, found):
                if min_l > (i - p + 1):
                    min_l = i - p + 1
                    rb = p
                    re = i
                found[s[p]] -= 1
                p += 1

        return s[rb:re+1]

    def is_valid_window(self, require, found):
        for i in require:
            if found[i] < require[i]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    #print s.minWindow('ADOBECODEBANC', 'ABC')
    #print s.minWindow('ADOBECODEBANC', 'ABCZ')
    #print s.minWindow('a', 'a')
    #print s.minWindow('a', 'b')
    #print s.minWindow('ab', 'A')
    #print s.minWindow('ab', 'b')
    #print s.minWindow('aa', 'aa')
    print s.minWindow("onlswwtraopuasovmrmdouldsqiryidoxpgtlcmnschswxpirbmfxzkqpsjncnebekupoheglmyhlqsctgirfsjunskrfotj", "apapyfvjtwtemnhf")
