#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        r = 0
        for i in range(32):
            ones = zeros = 0
            for n in nums:
                bit = n & (1 << i)
                if bit:
                    ones += 1
                else:
                    zeros += 1

            if ones > zeros:
                r |= (1<<i)

            if r & 0x80000000:
                r = -(r^0xffffffff) - 1

        return r


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([3,1,2,3,2,3,3])
    print s.majorityElement([-2147483648])
