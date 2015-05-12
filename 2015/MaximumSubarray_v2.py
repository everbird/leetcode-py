#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        return self.divid_and_conque(A, 0, len(A) - 1)

    def divid_and_conque(self, A, l, r):
        if l == r:
            return A[l]

        if l > r:
            return -2**31

        mid = (l + r) // 2
        s = 0
        max_l = 0
        for i in range(mid-1, l-1, -1):
            s += A[i]
            max_l = max(max_l, s)

        s = 0
        max_r = 0
        for i in range(mid+1, r+1):
            s += A[i]
            max_r = max(max_r, s)

        max_v = max_l + A[mid] + max_r
        return max(
            max_v,
            self.divid_and_conque(A, l, mid - 1),
            self.divid_and_conque(A, mid + 1, r)
        )


if __name__ == '__main__':
    s = Solution()
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print s.maxSubArray(a)

    a = [-2, -1]
    print s.maxSubArray(a)
