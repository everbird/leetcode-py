#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, str(num)))

        return num


def main():
    s = Solution()
    print s.addDigits(38)
    print s.addDigits(39)


if __name__ == '__main__':
    main()
