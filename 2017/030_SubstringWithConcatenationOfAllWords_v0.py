#!/usr/bin/env python
# encoding: utf-8

from collections import Counter, defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        d = {}
        k = len(words[0])
        len_s = len(s)
        len_w = len(words)

        if len_s == k:
            return [] if len_w > 1 else [0]

        d = Counter(words)

        r = []
        for i in range(len_s - k*len_w + 1):
            _s = s[i:i + k*len_w]
            if self.testString(_s, k, d):
                r.append(i)
        return r

    def testString(self, s, k, dict):
        len_s = len(s)
        i = 0
        d = defaultdict(int)
        while i <= len_s - k:
            w = s[i:i+k]
            if not dict.get(w) or d[w] == dict[w]:
                return False

            d[w] += 1
            i += k

        return True


if __name__ == '__main__':
    s = 'barfoothefoobarman'
    words = ["foo", "bar"]
    _s = Solution()
    r = _s.findSubstring(s, words)
    print r
