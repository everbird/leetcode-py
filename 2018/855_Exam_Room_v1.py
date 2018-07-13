#!/usr/bin/eni python
# encoding: utf-8


class ExamRoom(object):

    def __init__(self, N):
        self.n = N
        self.array = []

    def seat(self):
        if not self.array:
            index = 0
            self.array.append(index)
            return index

        length = len(self.array)
        max_d = self.array[0]
        index = 0
        p = 0
        for i in range(1, length):
            pre = self.array[i-1]
            d = (self.array[i] - pre) // 2
            if d > max_d:
                max_d = d
                index = pre + d
                p = i

        tail = self.n - 1 - self.array[-1]
        if tail > max_d:
            max_d = tail
            index = self.n - 1
            self.array.append(index)
            return index

        # s = m = 0
        # e = length - 1
        # while s <= e:
        #     m = (s + e) // 2
        #     v = self.array[m]
        #     if v >= index:
        #         e = m - 1
        #     elif v < index:
        #         s = m + 1

        # self.array.insert(s, index)
        self.array.insert(p, index)
        return index

    def leave(self, p):
        s = 0
        e = len(self.array) - 1
        if e == 0:
            self.array.pop()
            return

        while s <= e:
            m = (s + e) // 2
            if self.array[m] > p:
                e = m - 1
            elif self.array[m] < p:
                s = m + 1
            else:
                self.array.pop(m)
                break


def binary_search_insert(array, v):
    s = 0
    e = len(array)
    while s <= e:
        m = (s + e) // 2
        if array[m] == v:
            return m
        elif array[m] > v:
            e = m - 1
        else:
            s = m + 1

    return s


if __name__ == '__main__':
    s = ExamRoom(10)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(4)
    print s.seat()

    print '==' * 5
    s = ExamRoom(10)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(4)
    print s.seat()
    print s.seat()

    print '==' * 5
    s = ExamRoom(8)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(7)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()

    print '==' * 5
    s = ExamRoom(4)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(1)
    print s.leave(3)
    print s.seat()

    print '**' * 5

    print binary_search_insert([3, 9], 1)
    print binary_search_insert([0, 9], 4)
    print binary_search_insert([0, 4, 9], 2)
