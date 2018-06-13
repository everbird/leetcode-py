#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def longestMountain(self, A):
        last_up = last_down = up = down = 0
        pre = None
        max_m = 0

        def _check():
            if down > 0:
                last_down = down
                if last_up:
                    return max(max_m, last_up+last_down+1)
            return max_m

        for i in A:
            if pre is None:
                pre = i
                continue

            if i > pre:
                if down > 0:
                    max_m = _check()
                    down = 0
                up += 1
            elif i < pre:
                if up > 0:
                    last_up = up
                    up = 0
                down += 1
            else:
                max_m = _check()
                last_up = last_down = up = down = 0

            pre = i
            # print up, down, last_up, last_down, '<<<', i

        return _check()


def main():
    s = Solution()
    tests = [
        (
            [2,1,4,7,3,2,5],
            5
        ),
        (
            [2,2,2],
            0
        ),
        (
            [0,1,2,3,4,5,4,3,2,1,0],
            11
        ),
        (
            [0,0,1,0,0,1,1,1,1,1],
            3
        )
    ]
    for input_args, expected in tests:
        r = s.longestMountain(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


if __name__ == '__main__':
    main()
