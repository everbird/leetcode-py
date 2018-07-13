#!/usr/bin/eni python
# encoding: utf-8


import heapq


class ExamRoom(object):

    def __init__(self, N):
        self.n = N
        self.heap = []
        self.valid_tuples_by_start = {}
        self.valid_tuples_by_end = {}
        self.push(0, self.n - 1)

    def seat(self):
        priority, _start, _end, valid = self.pop()
        d = -priority
        index = _start+d
        if _start == 0:
            index = 0
            self.push(1, _end)
        elif _end == self.n - 1:
            if _start != _end:
                self.push(_start, _end - 1)
        else:
            if index > _start:
                self.push(_start, index - 1)

            if _end > index:
                self.push(index + 1, _end)

        print '>>>>', sorted(self.heap, key=lambda x: x[1]), index
        return index

    def push(self, start, end):
        if start == 0 or end == self.n - 1:
            _d = self.n - 1
        else:
            _d = (end - start) // 2

        t = [-_d, start, end, True]
        heapq.heappush(self.heap, t)

        self.valid_tuples_by_start[start] = t
        self.valid_tuples_by_start[end] = t

    def pop(self):
        while True:
            priority, _start, _end, valid = heapq.heappop(self.heap)
            if valid:
                del self.valid_tuples_by_start[_start]
                del self.valid_tuples_by_start[_end]
                return priority, _start, _end, valid

    def leave(self, p):
        start = end = p
        p_left = p - 1
        p_right = p + 1
        if p_left >= 0 and p_left in self.valid_tuples_by_end:
            t = self.valid_tuples_by_end.pop(p_left)
            t[3] = False
            start = t[1]

        if p_right < self.n and p_right in self.valid_tuples_by_start:
            t = self.valid_tuples_by_start.pop(p_right)
            t[3] = False
            end = t[2]

        self.push(start, end)
        print sorted(self.heap, key=lambda x: x[1]), '<<<<', p


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

def pp(rs):
    n = rs[0][0]
    solution = ExamRoom(n)
    for i in rs[1:]:
        if not i:
            print '[pp] solution.seat()'
            print solution.seat()
        else:
            print '[pp] solution.leave(%s)' % i[0]
            print solution.leave(i[0])



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

    print '==' * 5
    s = ExamRoom(10)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(4)
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(4)
    print s.seat()
    print s.seat()
    print s.leave(7)
    print s.seat()
    print s.leave(3)
    print s.seat()
    print s.leave(3)
    print s.seat()
    print s.leave(9)
    print s.seat()
    print s.leave(0)
    print s.leave(8)
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(8)
    print s.seat()
    print s.seat()
    print s.leave(2)

    print '==' * 5
    s = ExamRoom(10)
    print s.seat()
    print s.seat()
    print s.leave(0)
    print s.leave(9)
    print s.seat()

    print '==' * 5
    s = ExamRoom(1)
    print s.seat()
    print s.leave(0)
    print s.seat()

    print '**' * 5
    pp([[10],[],[],[9],[],[],[],[],[],[],[],[],[],[9],[],[1],[],[8],[],[2],[],[1],[],[0],[1],[],[],[7],[],[3],[],[7],[],[0],[3],[]])

    print '**' * 5
    pp([[10],[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0]])
