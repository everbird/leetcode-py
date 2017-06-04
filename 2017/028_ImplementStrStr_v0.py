#!/usr/bin/env python
# encoding: utf-8

def get_next(N, j):
    if j == 0:
        return -1
    i = get_next(N, j-1)
    while (N[i+1] != N[j] and i >= 0):
        i = get_next(N, i)

    return i + 1 if N[i+1] == N[j] else -1

def get_next_array_v1(s):
    r = [0] * len(s)
    for i, c in enumerate(s):
        r[i] = get_next(s, i)
    return r

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
            r[suf_i] = 0
            suf_i += 1
    return r

def get_next_array_v3(pattern):
    next_arr = [0] * len(pattern)
    pre_i, suf_i = 0, 1

    while suf_i < len(pattern):
        # Found prefix-suffix match.
        if pattern[pre_i] == pattern[suf_i]:
            next_arr[suf_i] = pre_i + 1
            pre_i, suf_i = pre_i + 1, suf_i + 1
        else:
            if pre_i:
                pre_i = next_arr[pre_i-1]
            else:
                next_arr[suf_i] = 0
                suf_i += 1

    return next_arr

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        NEXT = get_next_array_v2(needle)
        len_y = len(haystack)
        len_n = len(needle)
        n_index = 0
        i = 0
        while i < len_y:
            c = haystack[i]
            if c == needle[n_index]:
                n_index += 1
                i += 1

                if n_index == len_n:
                    return i - len_n

            if i < len_y and haystack[i] != needle[n_index]:
                if n_index == 0:
                    i += 1
                else:
                    n_index = NEXT[n_index - 1] + 1

        return -1

    def strStr_v1_timeout(self, haystack, needle):
        if not needle:
            return 0
        NEXT = get_next_array(needle)
        len_y = len(haystack)
        len_n = len(needle)
        n_index = 0
        for i, c in enumerate(haystack):
            while c != needle[n_index] and n_index > 0:
                print 'NEXT', n_index
                n_index = NEXT[n_index - 1] + 1

            if c == needle[n_index]:
                n_index += 1

            if n_index == len_n:
                return i - len_n + 1

        return -1

    def strStr_v0(self, haystack, needle):
        len_n = len(needle)
        len_h = len(haystack)
        for i in range(len_h - len_n + 1):
            if needle == haystack[i:i+len_n]:
                return i
        return -1


    def strStr_timeout(self, haystack, needle):
        if not needle:
            return 0

        len_needle = len(needle)
        len_haystack = len(haystack)
        for i, c in enumerate(haystack):
            needle_index = 0
            _index = i
            while needle_index < len_needle and _index < len_haystack and needle[needle_index] == haystack[_index]:
                needle_index += 1
                _index += 1

                if needle_index == len_needle:
                    return i

        return -1




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
    print get_next_array_v2(n)
    print get_next_array_v3(n)
