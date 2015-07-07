#!/usr/bin/env python
# encoding: utf-8


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.reverse_stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        store = []
        for i in range(self._size()):
            store.append(self._pop())

        self._push(x)
        for v in store[::-1]:
            self._push(v)

    # @return nothing
    def pop(self):
        self._pop()

    # @return an integer
    def peek(self):
        return self._peek()

    # @return an boolean
    def empty(self):
        return self._is_empty()

    def _push(self, v):
        self.reverse_stack.append(v)

    def _pop(self):
        return self.reverse_stack.pop()

    def _size(self):
        return len(self.reverse_stack)

    def _is_empty(self):
        return self._size() == 0

    def _peek(self):
        return self.reverse_stack[-1] if not self._is_empty() else None


if __name__ == '__main__':
    q = Queue()
    print q.empty()
    q.push(1)
    q.push(2)
    print q.peek()
    q.pop()
    print q.peek()
