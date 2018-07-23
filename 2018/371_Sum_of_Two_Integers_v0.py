#!/usr/bin/eni python
# encoding: utf-8



class Solution(object):
    def getSum(self, a, b):
        if a == 0:
            return b
        elif b == 0:
            return a

        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask
        r = 0
        carry = False
        n = 0
        while a or b:
            bit_a = a % 2
            bit_b = b % 2
            if bit_a and bit_b and carry:
                bit = 1
                carry = True
            elif (
                (bit_a and bit_b and not carry)
                or (carry and bit_a and not bit_b)
                or (carry and bit_b and not bit_a)

            ):
                bit = 0
                carry = True
            elif any([carry, bit_a, bit_b]):
                bit = 1
                carry = False
            else:
                bit = 0
                carry = False

            if bit:
                r = bit<<n | r

            n += 1
            a = a // 2
            b = b // 2

        if carry and n < 32:
            r = 1<<n | r

        if (r >> 31) & 1:
            return ~(r^mask)
        return r

    def getSum2(self, a, b):
        if a == 0:
            return b
        elif b == 0:
            return a

        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a^b) & mask, ((a&b)<<1) & mask

        if (a >> 31) & 1:
            return ~(a^mask)
        else:
            return a

if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                1,
                2
            ),
            3
        ),
        (
            (
                2,
                3
            ),
            5
        ),
        (
            (
                -1,
                1
            ),
            0
        ),
    ]
    f = s.getSum
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
