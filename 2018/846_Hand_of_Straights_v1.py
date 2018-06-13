#!/usr/bin/env python
# encoding: utf-8



class Solution(object):

    def isNStraightHand(self, hand, W):
        len_n = len(hand)
        if len_n % W > 0:
            return False

        _set = set(hand)
        c = dict()
        for x in hand:
            c[x] = 1 + c.get(x, 0)

        for i in range(len_n // W):
            min_k = min(_set)
            for j in range(W):
                _k = min_k + j
                # print c, _k, '<<<', min_k
                v = c.get(_k)
                if not v:
                    return False
                elif v == 1:
                    del c[_k]
                    _set.remove(_k)
                else:
                    c[_k] = c[_k] - 1

        return sum(c.values()) == 0


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
        (
            (
                range(120),
                3
            ),
            True
        ),
    ]
    for input_args, expected in tests:
        r = s.isNStraightHand(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


if __name__ == '__main__':
    main()
