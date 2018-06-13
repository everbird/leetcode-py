#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def backspaceCompare(self, S, T):
        len_s = len(S)
        len_t = len(T)
        cnt_s = cnt_t = 0
        index_s = len_s - 1
        index_t = len_t - 1
        while index_s >= 0 or index_t >= 0:
            if index_s >= 0 and S[index_s] == '#':
                cnt_s += 1
                index_s -= 1
                continue

            if index_t >= 0 and T[index_t] == '#':
                cnt_t += 1
                index_t -= 1
                continue

            if cnt_s > 0:
                cnt_s -= 1
                index_s -= 1
                continue
            elif cnt_t > 0:
                cnt_t -= 1
                index_t -= 1
            elif index_s >= 0 and index_t >= 0 and S[index_s] == T[index_t]:
                index_s -= 1
                index_t -= 1
            else:
                return False

        return index_s < 0 and index_t < 0


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
