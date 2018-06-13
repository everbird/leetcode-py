#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def pushDominoes(self, dominoes):
        len_n = len(dominoes)
        MAX_V = len_n + 1
        left_list = [MAX_V] * len_n
        right_list = [MAX_V] * len_n

        mark = None
        step = 0
        for i in range(len_n - 1, -1, -1):
            char = dominoes[i]
            if char == 'L' or char == 'R':
                mark = char
                step = 0
            elif char == '.' and mark == 'L':
                step += 1
                left_list[i] = step

        mark = None
        for i in range(len_n):
            char = dominoes[i]
            if char == 'L' or char == 'R':
                mark = char
                step = 0
            elif char == '.' and mark == 'R':
                step += 1
                right_list[i] = step

        _dominoes = list(dominoes)
        for i in range(len_n):
            char = _dominoes[i]
            left_v = left_list[i]
            right_v = right_list[i]
            if char == '.':
                if left_v < right_v:
                    _dominoes[i] = 'L'
                elif right_v < left_v:
                    _dominoes[i] = 'R'

        return ''.join(_dominoes)


def main():
    s = Solution()
    tests = [
        (
            ".L.R...LR..L..",
            "LL.RR.LLRRLL.."
        ),
        (
            ".L.R.",
            "LL.RR"
        ),
    ]
    for input_args, expected in tests:
        r = s.pushDominoes(input_args)
        print 'Input:{}\tOutput:{}\tExpected:{}'.format(input_args, r, expected)


if __name__ == '__main__':
    main()
