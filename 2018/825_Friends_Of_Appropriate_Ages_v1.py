#!/usr/bin/eni python
# encoding: utf-8


from collections import Counter, defaultdict


class Solution(object):

    def numFriendRequests(self, ages):
        u_ages = set(ages)
        c = Counter(ages)
        cnt = 0
        age_requests = defaultdict(set)
        for age_b in u_ages:
            for age_a in u_ages:
                if should_request(age_b, age_a):
                    age_requests[age_b].add(age_a)

        for age_b, request_ages in age_requests.iteritems():
            cb = c[age_b]
            cnt += cb * sum([
                c[age_a] for age_a in request_ages]
            )
            if should_request(age_b, age_b):
                cnt -= cb

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
