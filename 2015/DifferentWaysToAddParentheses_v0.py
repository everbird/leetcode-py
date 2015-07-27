#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        ret = []
        for i in range(len(input)):
            c = input[i]
            if c in ('+', '-', '*'):
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for li in left:
                    for ri in right:
                        r = 0
                        if c == '+':
                            r = int(li) + int(ri)
                        elif c == '-':
                            r = int(li) - int(ri)
                        elif c == '*':
                            r = int(li) * int(ri)
                        ret.append(r)
        if not ret:
            ret.append(int(input))

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.diffWaysToCompute('2-1-1')
    print s.diffWaysToCompute('2*3-4*5')
