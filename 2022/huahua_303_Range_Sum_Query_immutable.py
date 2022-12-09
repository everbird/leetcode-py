#!/usr/bin/env python3

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self._sum = [0] * (n+1)
        self._sum[0] = 0
        for i in range(n):
            self._sum[i+1] = self._sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return 0

        return self._sum[right+1] - self._sum[left]

# range edge
