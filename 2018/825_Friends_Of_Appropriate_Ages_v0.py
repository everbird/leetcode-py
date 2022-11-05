#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def numFriendRequests(self, ages):
        len_a = len(ages)
        cnt = 0
        for i in xrange(len_a-1):
            for j in xrange(i+1, len_a):
                if i == j:
                    continue
                if should_request(ages[i], ages[j]):
                    cnt += 1
                if should_request(ages[j], ages[i]):
                    cnt += 1
        return cnt


def should_request(age_b, age_a):
    return not (
        age_b <= (0.5 * age_a + 7)
        or age_b > age_a
        or (age_b > 100 and age_a < 100)
    )



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [16, 16],
            2
        ),
        (
            [16, 17, 18],
            2
        ),
        (
            [20,30,100,110,120],
            3
        ),
    ]
    f = s.numFriendRequests
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
