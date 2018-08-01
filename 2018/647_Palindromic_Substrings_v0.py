#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        cnt = 0
        for j in range(n):
            for i in range(j+1):
                if is_palindrome(s, i, j):
                    cnt +=1

        return cnt


def is_palindrome(s, start, end):
    while start < end and s[start] == s[end]:
        start += 1
        end -= 1

    return start >= end



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            'abc',
            3
        ),
        (
            'aaa',
            6
        ),
    ]
    f = s.countSubstrings
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
