#!/usr/bin/eni python
# encoding: utf-8


import heapq


class ExamRoom(object):

    def __init__(self, N):
        self.n = N
        self.heap = [(-1, -1, None)]
        self.seats = set([])

    def seat(self):
        priority, _start, dis = heapq.heappop(self.heap)
        d = -priority

        index = _start + d
        if _start == -1:
            if dis is None:
                _d = self.n - 1
            else:
                _d = dis//2
            index = 0
            heapq.heappush(self.heap, (-_d, 0, dis))
        elif dis is None:
            _dis = self.n - 1 - _start
            _d = _dis // 2
            heapq.heappush(self.heap, (-_d, _start, _dis))
        else:
            _dis = d
            _d = _dis // 2
            heapq.heappush(self.heap, (-_d, _start, _dis))

            _dis2 = dis - d
            _d2 = _dis2 // 2
            heapq.heappush(self.heap, (-_d2, index, _dis2))

        # print '>>>>', sorted(self.heap, key=lambda x: x[1]), index
        return index

    def leave(self, p):
        if len(self.heap) == 1 and (
            self.heap[0][1] == -1
            or self.heap[0][2] is None
        ):
            self.heap = [(-1, -1, None)]
            return

        p_t = pre_t = None
        p_i = pre_i = -1
        min_delta = self.n
        for i, t in enumerate(self.heap):
            index = t[1]
            if index == p:
                p_t, p_i = t, i
            elif index < p:
                delta = p - index
                if delta < min_delta:
                    min_delta = delta
                    pre_t, pre_i = t, i

        if p == 0:
            d, _start, dis = p_t
            new_t = (-dis, -1, dis)
            self.heap[p_i] = new_t
        elif p == (self.n - 1):
            pre = pre_t[1]
            dis = self.n - 1 - pre
            new_t = (-dis, pre, None)
            self.heap[pre_i] = new_t
        else:
            # print self.heap, pre_t, p_t, '<<<'
            pre = pre_t[1]

            p_dis = p_t[2]
            pre_dis = pre_t[2]

            self.heap[p_i] = None
            self.heap[pre_i] = None
            self.heap = [x for x in self.heap if x is not None]
            new_dis = p_dis + pre_dis if p_dis else None
            new_index = pre
            new_d = new_dis // 2 if p_dis else (self.n - 1 - pre)
            new_t = (-new_d, new_index, new_dis)
            self.heap.append(new_t)

        heapq.heapify(self.heap)
        # print sorted(self.heap, key=lambda x: x[1]), '<<<<', p


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
