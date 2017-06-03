#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        NEXT = get_next_array_v2(needle)
        len_y = len(haystack)
        len_n = len(needle)
        n_index = 0
        i = 0
        while i < len_y and n_index < len_n:

            if haystack[i] == needle[n_index]:
                n_index += 1
                i += 1
            elif n_index > 0:
                n_index = NEXT[n_index - 1] + 1
            else:
                i += 1

        return i - len_n if n_index == len_n else -1

def get_next_array_v2(s):
    len_s = len(s)
    r = [-1] * len_s
    pre_i, suf_i = 0, 1
    while suf_i < len_s:
        if s[pre_i] == s[suf_i]:
            r[suf_i] = pre_i
            pre_i += 1
            suf_i += 1
        elif pre_i:
            pre_i = r[pre_i - 1] + 1
        else:
            r[suf_i] = -1
            suf_i += 1
    return r


if __name__ == '__main__':
    h = 'akfdsadfhklh'
    n = 'dsad'
    h = 'mississippi'
    n = 'issip'
    #h = 'aabaaaababaababaa'
    #n = 'bbbb'
    #h = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    #n = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    s = Solution()
    r = s.strStr(h, n)
    print r
    print s.create_next(n)
