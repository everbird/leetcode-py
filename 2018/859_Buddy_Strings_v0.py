#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def buddyStrings(self, A, B):
        len_a = len(A)
        len_b = len(B)
        if len_a != len_b:
            return False

        diffs = []
        d = {}
        dup = False
        for i in range(len_a):
            if A[i] != B[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
            if d.get(A[i]):
                dup = True
            d[A[i]] = True

        if len(diffs) == 2:
            i, j = diffs
            return A[i] == B[j] and A[j] == B[i]

        if not diffs:
            return dup

        return False


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                'ab',
                'ba'
            ),
            True
        ),
        (
            (
                'ab',
                'ab'
            ),
            False
        ),
        (
            (
                'aa',
                'aa'
            ),
            True
        ),
        (
            (
                'aaaaaaabc',
                'aaaaaaacb'
            ),
            True
        ),
        (
            (
                '',
                'ab'
            ),
            False
        ),
        (
            (
                'ab',
                'ca'
            ),
            False
        ),
    ]
    for input_args, expected in tests:
        r = s.buddyStrings(*input_args)
        result = r == expected
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(result, input_args, r, expected)
