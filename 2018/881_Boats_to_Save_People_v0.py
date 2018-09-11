#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def numRescueBoats(self, people, limit):
        people = sorted(people)
        size = len(people)
        s = 0
        e = size - 1
        cnt = 0
        while s <= e:
            if people[s] + people[e] <= limit:
                s += 1
                e -= 1
            else:
                e -= 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 2],
                3
            ),
            1
        ),
        (
            (
                [3,2,2,1],
                3
            ),
            3
        ),
        (
            (
                [3,5,3,4],
                5
            ),
            4
        ),
    ]
    f = s.numRescueBoats
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
