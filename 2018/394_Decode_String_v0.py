#!/usr/bin/eni python
# encoding: utf-8


MODE_NUM = 1
MODE_CHAR = 2

class Solution(object):
    def decodeString(self, s):
        stack = []
        buf = ''
        mode = MODE_NUM
        for ch in s:
            if ch in '0123456789':
                if mode == MODE_CHAR:
                    stack.append((mode, buf))
                    buf = ''

                mode = MODE_NUM
                buf += ch
            elif ch == '[':
                stack.append((mode, int(buf)))
                buf = ''
            elif ch == ']':
                pre_mode, pre_v = stack.pop()
                if pre_mode == MODE_NUM:
                    buf = buf * pre_v

                if stack and stack[-1][0] == MODE_CHAR:
                    _, v = stack.pop()
                    buf = v + buf
            else:
                mode = MODE_CHAR
                buf += ch

        return buf



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            '3[a]2[bc]',
            'aaabcbc'
        ),
        (
            '3[a2[c]]',
            'accaccacc'
        ),
        (
            '2[abc]3[cd]ef',
            'abcabccdcdcdef'
        ),
    ]
    f = s.decodeString
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
