#!/usr/bin/env python3

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dt = defaultdict(list)
        self.dv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[key].append(timestamp)
        self.dv[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        index = binary_search_lower_nearest(self.dt[key], timestamp)
        return self.dv[key][index] if index >=0 else ""
        

def binary_search_lower_nearest(nums, x):
    n = len(nums)
    if not n:
        return -1

    if x >= nums[-1]:
        return n-1
    elif x < nums[0]:
        return -1
    
    s = 0
    e = n - 1
    while s < e-1:
        m = (s - e) // 2 + e
        if nums[m] <= x:
            s = m
        else:
            e = m
    return s
