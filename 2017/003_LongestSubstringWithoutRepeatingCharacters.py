#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        max_length = 0
        pos = {}
        start = 0
        for i, c in enumerate(s):
            pre_pos = pos.get(c)
            pos[c] = i
            if pre_pos is not None and pre_pos >= start:
                start = pre_pos + 1
            else:
                current_length = i - start + 1
                max_length = max(max_length, current_length)
        return max_length


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring('abcabcbb')
    print r
    r = s.lengthOfLongestSubstring('zaabcabcabcz')
    print r
