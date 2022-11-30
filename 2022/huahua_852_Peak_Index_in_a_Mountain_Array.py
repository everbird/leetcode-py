#!/usr/bin/env python3

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        e = n - 1
        while s <= e:
            m = (s+e) // 2

            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m

            if arr[m] < arr[m+1]:
                s = m + 1
            else:
                e = m

        return
