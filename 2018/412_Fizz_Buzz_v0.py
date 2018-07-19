#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def fizzBuzz(self, n):
        r = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                r.append('FizzBuzz')
            elif i % 3 == 0:
                r.append('Fizz')
            elif i % 5 == 0:
                r.append('Buzz')
            else:
                r.append(str(i))
        return r



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz"
            ]
        ),
    ]
    f = s.fizzBuzz
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
