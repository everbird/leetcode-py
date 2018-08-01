import random
import bisect


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = []
        s = 0
        for n in w:
            s += n
            self.w.append(s)


    def pickIndex(self):
        """
        :rtype: int
        """
        t = random.randint(1, self.w[-1])
        # return bisect.bisect_left(self.w, t)
        return binary_search_left(self.w, t)


def binary_search_left(nums, t):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        v = nums[mid]
        if v == t:
            return mid
        elif v > t:
            hi = mid
        else:
            lo = mid + 1
    return lo



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
