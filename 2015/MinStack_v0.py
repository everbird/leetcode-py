#!/usr/bin/env python
# encoding: utf-8


class MinStack:

    def __init__(self):
        self.s = []
        self.min_v = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        d = None if self.min_v is None else x - self.min_v
        self.min_v = min(self.min_v, x) if self.min_v is not None else x
        self.s.append((x, d))
        return x

    # @return nothing
    def pop(self):
        v, d = self.s.pop()
        self.min_v = v - d if self.s else None

    # @return an integer
    def top(self):
        return self.s[-1][0] if self.s else None


    # @return an integer
    def getMin(self):
        return self.min_v

if __name__ == '__main__':
    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)
    print '>>>', s.s
    print s.getMin()
    s.pop()
    print s.getMin()

    print '-' * 6
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-1)
    print '>>>', s.s
    print s.getMin()
    print s.top()
    s.pop()
    print s.getMin()
