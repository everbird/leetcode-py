#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def findKthNumber(self, n, k):
        current = 1
        k = k - 1
        while k > 0:
            steps = cal_steps(n, current, current+1)

            if k >= steps:
                k -= steps
                current += 1
            else:
                current *= 10
                k -= 1

        return current

def cal_steps(n, n1, n2):
    steps = 0
    while n1 <= n:
        steps += min(n+1, n2) - n1
        n1 *= 10
        n2 *= 10

    return steps



def transfer(x, n):
    if x*10 <= n:
        return x*10

    if x >= n:
        x //= 10

    x += 1
    while x % 10 == 0:
        x //= 10
    return x


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                13,
                2
            ),
            10
        ),
        (
            (
                10,
                3
            ),
            2
        ),
        (
            (
                9885387,
                8786251
            ),
            1
        ),
    ]
    f = s.findKthNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
