#!/usr/bin/env python
# encoding: utf-8


class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.s.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)
        return x

    # @return nothing
    def pop(self):
        v = self.s.pop()
        if v == self.mins[-1]:
            self.mins.pop()

    # @return an integer
    def top(self):
        return self.s[-1] if self.s else None

    # @return an integer
    def getMin(self):
        return self.mins[-1] if self.mins else None

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
