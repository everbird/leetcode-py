#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            n = tokens[i]
            if n in ('+', '-', '*', '/'):
                a1 = stack.pop()
                a2 = stack.pop()
                if n == '+':
                    stack.append(a2+a1)
                elif n == '-':
                    stack.append(a2-a1)
                elif n == '*':
                    stack.append(a2*a1)
                elif n == '/':
                    symbol = 1 if a1*a2 > 0 else -1
                    v = abs(a2)/abs(a1)
                    stack.append(v*symbol)
            else:
                stack.append(int(n))

        return stack[0] if stack else 0


if __name__ == '__main__':
    s = Solution()
    #print s.evalRPN(["2", "1", "+", "3", "*"])
    #print s.evalRPN(["4", "13", "5", "/", "+"])
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
