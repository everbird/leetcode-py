#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        len_n2 = len(num2)
        s = "0"
        for i in range(len_n2 - 1, -1, -1):
            char = num2[i]
            r = self.multiply_single_num(num1, char)
            filled_zeros = len_n2 - 1 - i
            r = r + '0' * filled_zeros
            s = self.add(s, r)
        return s


    def multiply_single_num(self, num, single_num):
        len_n = len(num)
        carry = 0
        s = ""
        for i in range(len_n - 1, -1, -1):
            char = num[i]
            r = self.multiply_chars(char, single_num) + carry
            carry = r // 10
            rn = r % 10
            s = str(rn) + s
        if carry:
            s = str(carry) + s
        return s


    def multiply_chars(self, char1, char2):
        return int(char1) * int(char2)


    def add(self, num1, num2):
        len_n1 = len(num1)
        len_n2 = len(num2)
        len_max = max(len_n1, len_n2)
        carry = 0
        s = ""
        for i in range(len_max):
            n1 = int(num1[len_n1 - i - 1]) if i < len_n1 else 0
            n2 = int(num2[len_n2 - i - 1]) if i < len_n2 else 0
            r =  n1 + n2 + carry
            carry = r // 10
            rn = r % 10
            s = str(rn) + s
        if carry:
            s = str(carry) + s
        return s


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
