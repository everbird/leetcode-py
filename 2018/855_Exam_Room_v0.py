#!/usr/bin/eni python
# encoding: utf-8


# Time Limit Exceeded
class ExamRoom(object):

    def __init__(self, N):
        self.n = N
        self.array = [False] * N

    def seat(self):
        index, max_d = -1, 0
        pre = None
        for i, s in enumerate(self.array):
            if s:
                if pre is None:
                    pre = i
                    max_d = i
                    if max_d > 0:
                        index = 0
                    continue

                d = (i - pre) // 2
                if d > max_d:
                    max_d = d
                    index = pre + d
                pre = i

        if pre is None:
            index = 0
        elif pre == 0:
            index = self.n - 1
        else:
            d = self.n - 1 - pre
            if d > max_d:
                max_d = d
                index = self.n - 1

        self.array[index] = True
        # print '>>>', self.array
        return index

    def leave(self, p):
        self.array[p] = False


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
