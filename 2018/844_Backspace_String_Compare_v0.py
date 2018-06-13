#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def backspaceCompare(self, S, T):
        return get_actual_str(S) == get_actual_str(T)


def get_actual_str(s):
    len_s = len(s)
    index = len_s - 1
    cnt = 0
    r = []
    while index >= 0:
        char = s[index]
        if char == '#':
            cnt += 1
        elif cnt > 0:
            cnt -= 1
        else:
            r.append(char)
        index -= 1

    return ''.join(r)


def main():
    s = Solution()
    tests = [
        (
            (
                "ab#c",
                "ad#c"
            ),
            True
        ),
        (
            (
                "ab##",
                "c#d#"
            ),
            True
        ),
        (
            (
                "a##c",
                "#a#c"
            ),
            True
        ),
        (
            (
                "a#c",
                "b"
            ),
            False
        ),
    ]
    for input_args, expected in tests:
        r = s.backspaceCompare(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


if __name__ == '__main__':
    main()
