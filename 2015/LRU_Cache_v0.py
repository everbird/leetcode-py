#!/usr/bin/env python
# encoding: utf-8

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cycle = []

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
        if key not in self.cycle:
            if len(self.cycle) >= self.capacity:
                self.cache.pop(self.cycle[0])
                self.cycle = self.cycle[1:]

            self.cycle.append(key)
        else:
            self.promote(key)


        self.cache[key] = value

    def promote(self, key):
        pos = self.cycle.index(key)
        self.cycle = self.cycle[:pos] + self.cycle[pos+1:] + [key]


if __name__ == '__main__':
    s = LRUCache(3)
    s.set('a', 1)
    s.set('b', 2)
    s.set('c', 3)
    print s.get('a')
    s.set('d', 4)
    print s.cycle, s.cache

    print '-' * 6
    s = LRUCache(2)
    s.set(2,1)
    s.set(1,1)
    s.set(2,3)
    s.set(4,1)
    print s.get(1)
    print s.get(2)
    print '>>>', s.cache, s.cycle

