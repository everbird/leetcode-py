#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        lend = len(digits)
        carry = 0
        for i in range(lend - 1, -1, -1):
            if i == lend - 1:
                v = digits[i] + 1
            else:
                v = digits[i] + carry

            digits[i] = v % 10
            carry = v // 10

        if carry:
            return [carry] + digits
        else:
            return digits


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([1,2,3])
    print s.plusOne([9,9])
