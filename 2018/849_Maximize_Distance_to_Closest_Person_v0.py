#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def maxDistToClosest(self, seats):
        max_d = 0
        pre = None
        len_n = len(seats)
        for i in range(len_n):
            v = seats[i]
            if v:
                if pre is None:
                    pre = i
                    max_d = max(max_d, i)
                else:
                    d = i - pre
                    max_d = max(max_d, d//2)
                    pre = i

        return max(max_d, len_n-1-pre)


def main():
    s = Solution()
    tests = [
        (
            [1,0,0,0,1,0,1],
            2
        ),
        (
            [1,0,0,0],
            3
        ),
        (
            [1,0,0,1],
            1
        )
    ]
    for input_args, expected in tests:
        r = s.maxDistToClosest(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)

if __name__ == '__main__':
    main()
