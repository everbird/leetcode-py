#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        mod9 = num % 9

        if num == 0:
            return 0

        if mod9 == 0:
            return 9

        return mod9


def main():
    s = Solution()
    print s.addDigits(38)
    print s.addDigits(39)


if __name__ == '__main__':
    main()
