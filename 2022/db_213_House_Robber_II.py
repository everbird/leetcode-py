#!/usr/bin/env python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        global cache
        cache = {}
        return rob_house(nums, 0, len(nums)-1)

cache = {}

def rob_house(nums, s, e):
    global cache
    if cache.get((s, e)):
        return cache.get((s, e))

    n = len(nums)
    if s > e:
        return 0
    if s == e:
        return nums[s]
    if s+1 == e:
        return max(nums[s], nums[e])

    if s == 0:
        v1 = nums[s] + rob_house(nums, s+2, e-1) 
    else:
        v1 = nums[s] + rob_house(nums, s+2, e)
   
    v2 = rob_house(nums, s+1, e)
    r = max(
        v1,
        v2,
    )
    cache[(s, e)] = r
    return r

# 74/75 TLE
