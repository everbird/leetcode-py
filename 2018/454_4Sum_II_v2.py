#!/usr/bin/eni python
# encoding: utf-8


#  Time Limit Exceeded
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        A = sorted(A)
        B = sorted(B)
        d_cnt = 0
        d_cache = {}
        c_cache = {}
        b_cache = {}
        for d in D:
            target_1 = 0 - d
            if d_cache.get(target_1):
                d_cnt += d_cache[target_1]
                continue

            c_cnt = 0
            for c in C:
                target_2 = target_1 - c

                if c_cache.get(target_2):
                    c_cnt += c_cache[target_2]
                    continue

                b_cnt = 0
                for b in B:
                    target_3 = target_2 - b

                    if b_cache.get(target_3):
                        b_cnt += b_cache[target_3]
                        continue

                    cnt = 0
                    for a in A:
                        if a == target_3:
                            cnt += 1
                    b_cache[target_3] = cnt
                    b_cnt += cnt

                c_cache[target_2] = b_cnt
                c_cnt += b_cnt

            d_cache[target_1] = c_cnt
            d_cnt += c_cnt

        # print '>>', d_cache
        # print '>>', c_cache
        # print '>>', b_cache

        return d_cnt


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,2],
                [-2,-1],
                [-1,2],
                [0,2],
            ),
            2
        ),
        (
            (
                [0,1,-1],
                [-1,1,0],
                [0,0,1],
                [-1,1,1],
            ),
            17
        ),
        (
            (
                [1,1,-1,-1],
                [-1,-1,1,1],
                [1,-1,0,-1],
                [1,1,-1,1],
            ),
            76
        ),
    ]
    for input_args, expected in tests:
        r = s.fourSumCount(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
