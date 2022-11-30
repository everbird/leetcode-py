#!/usr/bin/env python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs():
            s = 0
            e = len(nums)-1
            while s <= e:
                m = (s+e) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    if target >= nums[s] or nums[m] <= nums[e]:
                        e = m - 1
                    else:
                        s = m + 1
                elif nums[m] < target:
                    if nums[m] >= nums[s] or target <= nums[e]:
                        s = m + 1
                    else:
                        e = m - 1

            return -1

        return bs()
