#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        left_nearest_steps = []
        d = {}
        for i, x in enumerate(s):
            pre = d.get(x)
            if pre is not None:
                steps = i - pre
            else:
                steps = 0
            left_nearest_steps.append((x, steps))

            d[x] = i

        longest = 0
        for i, (char, step) in enumerate(left_nearest_steps):
            tmp = self.get_length(left_nearest_steps[:-step if step > 0 else None])
            if tmp > longest:
                longest = tmp

        return longest

    def get_length(self, char_steps):
        if not char_steps:
            return 0

        char, steps = char_steps[-1]
        if steps == 0:
            return self.get_length(char_steps[:-1]) + 1
        else:
            return self.get_length(char_steps[-steps:-1]) + 1


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring('abcabcbb')
    print r
    r = s.lengthOfLongestSubstring('zaabcabcabcz')
    print r
