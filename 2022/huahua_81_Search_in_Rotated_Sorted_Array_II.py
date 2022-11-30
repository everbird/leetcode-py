#!/usr/bin/env python3

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def bs():
            s = 0
            e = len(nums)-1
            while s <= e:
                # Shrink
                while s < e and nums[s] == nums[s+1]:
                    s += 1
                while s < e and nums[e] == nums[e-1]:
                    e -= 1

                m = (s+e)//2
                if nums[m] == target:
                    return True

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

            return False

        return bs()
