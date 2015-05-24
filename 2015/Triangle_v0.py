#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        lent = len(triangle)
        return min(self.get_min_heights(triangle, lent-1))

    def get_min_heights(self, triangle, level):
        rs = []
        if level == 0:
            return triangle[0]

        items = self.get_min_heights(triangle, level-1)
        nums = triangle[level]
        for i in range(len(nums)):
            n = nums[i]
            l = items[i-1] if i-1 >= 0 else None
            r = items[i] if i < len(items) else None
            if l is None:
                rs.append(r+n)

            elif r is None:
                rs.append(l+n)

            else:
                rs.append(min(l, r)+n)

        return rs


if __name__ == '__main__':
    s = Solution()
    #t = [
        #[2],
        #[3,4],
        #[6,5,7],
        #[4,1,8,3]
    #]
    #print s.minimumTotal(t)

    t = [
        [1],
        [-5,-2],
        [3,6,1],
        [-1,2,4,-3]
    ]
    print s.minimumTotal(t)
