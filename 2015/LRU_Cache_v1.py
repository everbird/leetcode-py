#!/usr/bin/env python
# encoding: utf-8

from collections import OrderedDict


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    # @return an integer
    def get(self, key):
        r = self.cache.get(key)
        if r is not None:
            self.promote(key)

        return r if r is not None else -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                self.cache[key] = value
        else:
            self.promote(key)

        self.cache[key] = value

    def promote(self, key):
        v = self.cache.pop(key)
        self.cache[key] = v


if __name__ == '__main__':
    s = LRUCache(3)
    s.set('a', 1)
    s.set('b', 2)
    s.set('c', 3)
    print s.get('a')
    s.set('d', 4)

    print '-' * 6
    s = LRUCache(2)
    s.set(2,1)
    s.set(1,1)
    print s.cache
    s.set(2,3)
    print s.cache
    s.set(4,1)
    print s.get(1)
    print s.get(2)
    print s.cache

