#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def advantageCount(self, A, B):
        _A = sorted(A)
        _B = sorted(B)
        index = 0
        take = defaultdict(list)
        remain = []
        for a in _A:
            if a > _B[index]:
                take[_B[index]].append(a)
                index += 1
            else:
                remain.append(a)

        return [take[b].pop() if take[b] else remain.pop() for b in B]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [2,7,11,15],
                [1,10,4,11]
            ),
            [2,11,7,15]
        ),
        (
            (
                [12,24,8,32],
                [13,25,32,11]
            ),
            [24,32,8,12]
        ),
        (
            (
                [0],
                [0]
            ),
            [0]
        ),
    ]
    f = s.advantageCount
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
