#!/usr/bin/eni python
# encoding: utf-8


from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        c = Counter(tasks)
        a = [c.get(chr(ord('A')+x), 0) for x in range(26)]
        a.sort()
        time = 0
        while a[-1] > 0:
            i = 0
            while i <= n and a[-1] > 0:
                if i <= 25 and a[-i-1] > 0:
                    a[-i-1] -= 1
                i += 1
                time += 1
            a.sort()

        return time


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                ["A","A","A","B","B","B"],
                2
            ),
            8
        ),
    ]
    f = s.leastInterval
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
