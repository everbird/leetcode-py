#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        b = 0
        e = x
        while b <= e:
            mid = (b + e) // 2
            if mid*mid == x:
                return mid

            elif mid*mid > x:
                e = mid - 1
            else:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    b = mid + 1

        return mid


if __name__ == '__main__':
    s = Solution()
    print s.mySqrt(9)
