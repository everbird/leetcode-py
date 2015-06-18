#!/usr/bin/env python
# encoding: utf-8


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._enqueu(x)
        size = self._size()
        for i in range(size-1):
            self._enqueu(self._dequeue())

    # @return nothing
    def pop(self):
        if self._is_empty():
            return

        return self._dequeue()

    # @return an integer
    def top(self):
        if self._is_empty():
            return

        return self._peek()

    # @return an boolean
    def empty(self):
        return self._is_empty()

    def _enqueu(self, x):
        self.queue.append(x)

    def _dequeue(self):
        x = self.queue[0]
        self.queue = self.queue[1:]
        return x

    def _size(self):
        return len(self.queue)

    def _is_empty(self):
        return not bool(self.queue)

    def _peek(self):
        return self.queue[0]
