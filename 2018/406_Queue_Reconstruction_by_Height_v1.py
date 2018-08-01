#!/usr/bin/eni python
# encoding: utf-8



class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))  # deal with highest first
        r = []
        for x in people:
            r.insert(x[1], x)
        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        ),
    ]
    f = s.reconstructQueue
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
