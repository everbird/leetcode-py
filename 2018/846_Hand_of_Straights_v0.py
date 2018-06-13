#!/usr/bin/env python
# encoding: utf-8


from collections import Counter


class Solution(object):

    def isNStraightHand(self, hand, W):
        len_n = len(hand)
        if len_n % W > 0:
            return False

        c = Counter(hand)
        for i in range(len_n // W):
            min_k = min_nonzero(c)
            for j in range(W):
                _k = min_k + j
                # print c, _k, '<<<', min_k
                if not c.get(_k):
                    return False
                c.update({_k: -1})

        return sum(c.values()) == 0


def min_nonzero(c):
    min_k = None
    min_cnt = None
    for k, cnt in c.iteritems():
        if cnt > 0:
            if min_k is None or k < min_k:
                min_k = k
                min_cnt = cnt
    return min_k



def main():
    s = Solution()
    tests = [
        (
            (
                [1,2,3,6,2,3,4,7,8],
                3
            ),
            True
        ),
        (
            (
                [1,2,3,4,5],
                4
            ),
            False
        ),
        (
            (
                [8,6,5,7,9],
                5
            ),
            True
        ),
    ]
    for input_args, expected in tests:
        r = s.isNStraightHand(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


if __name__ == '__main__':
    main()
