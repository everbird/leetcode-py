#!/usr/bin/env python
# encoding: utf-8

import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = reduce(operator.xor, nums)
        i = 0
        while m % 2 == 0:
            m = m // 2
            i += 1

        def bit_distingush(x, i):
            return bool((x // (2**i)) % 2)
        a = [x for x in nums if bit_distingush(x, i)]
        b = [x for x in nums if not bit_distingush(x, i)]
        _a = reduce(operator.xor, a)
        _b = reduce(operator.xor, b)
        return [_a, _b]


def main():
    nums = [1, 2, 1, 3, 2, 5]
    s = Solution()
    print s.singleNumber(nums)


if __name__ == '__main__':
    main()
