#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        max_length = start = 0
        m = {}
        for i, c in enumerate(s):
            pos = m.get(c)
            if pos is not None and pos >= start:
                start = pos + 1
            else:
                max_length = max(max_length, i - start + 1)

            m[c] = i

        return max_length


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring('abcabcbb')
    print r
    r = s.lengthOfLongestSubstring('zaabcabcabcz')
    print r
    r = s.lengthOfLongestSubstring('z')
    print r
    r = s.lengthOfLongestSubstring('')
    print r
