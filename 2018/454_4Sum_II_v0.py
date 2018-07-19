#!/usr/bin/eni python
# encoding: utf-8


#  Time Limit Exceeded
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        A = sorted(A)
        B = sorted(B)
        r = set([])
        cnt = 0
        for i, d in enumerate(D):
            target_1 = 0 - d
            for j, c in enumerate(C):
                target_2 = target_1 - c
                ia = 0
                ib = n - 1
                stack = [(ia, ib)]
                while stack:
                    _ia, _ib = stack.pop()
                    if _ia >= n or _ib < 0:
                        continue

                    # print '>>>', _ia, _ib, A, B
                    s = A[_ia] + B[_ib]
                    if s > target_2:
                        stack.append((_ia, _ib-1))
                    elif s < target_2:
                        stack.append((_ia+1, _ib))
                    elif s == target_2:
                        cnt += 1
                        r.add((_ia, _ib, j, i))
                        stack.append((_ia+1, _ib))
                        stack.append((_ia, _ib-1))

        return len(r)


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
