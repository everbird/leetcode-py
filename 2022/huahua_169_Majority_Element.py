#!/usr/bin/env python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        maj = nums[0]
        for n in nums[1:]:
            if n == maj:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    maj = n

        return maj
