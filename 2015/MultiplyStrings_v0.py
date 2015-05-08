#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'

        if len(num2) == 1:
            return self._multiply(num1, num2[0])

        last = num2[-1]
        r1 = self.multiply(num1, num2[:-1])
        r2 = self._multiply(num1, last)

        return self.add(r1 + '0', r2)

    def add(self, num1, num2):
        lenn1 = len(num1)
        lenn2 = len(num2)
        count = max(lenn1, lenn2)
        ord0 = ord('0')
        carry = 0
        r = ''
        for i in range(1, count+1):
            n1 = ord(num1[-i]) - ord0 if i <= lenn1 else 0
            n2 = ord(num2[-i]) - ord0 if i <= lenn2 else 0
            t = n1 + n2 + carry
            carry = t // 10
            r = str(t % 10) + r

        return str(carry) + r if carry else r

    def _multiply(self, num1, digit):
        r = ''
        carry = 0
        di = ord(digit) - ord('0')
        for n in num1[::-1]:
            ni = ord(n) - ord('0')
            t = ni * di + carry
            carry = t // 10
            r = str(t % 10) + r

        return str(carry) + r if carry else r


if __name__ == '__main__':
    s = Solution()
    print s.multiply('7', '6')
    print s.multiply('22', '6')
    print s.multiply('6', '22')
    print s.multiply('12345', '54321')
    print s.add('120', '12')
    print s.multiply('123', '456')
    print s.add('4920', '615')
    print s.multiply('123', '0')
