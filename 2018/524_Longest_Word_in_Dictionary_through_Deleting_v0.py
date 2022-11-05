#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def findLongestWord(self, s, d):
        answer = ""
        max_len = 0
        for w in d:
            if is_subsequence(s, w):
                if len(w) > max_len:
                    answer = w
                    max_len = len(w)
                elif len(w) == max_len and answer > w:
                    answer = w

        return answer


def is_subsequence(s, w):
    w_len = len(w)
    w_index = 0
    for ch in s:
        if ch == w[w_index]:
            w_index += 1

        if w_index == w_len:
            break

    return w_index == w_len


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "abpcplea",
                ["ale","apple","monkey","plea"]
            ),
            "apple"
        ),
        (
            (
                "abpcplea",
                ["a","b","c"]
            ),
            "a"
        ),
    ]
    f = s.findLongestWord
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
