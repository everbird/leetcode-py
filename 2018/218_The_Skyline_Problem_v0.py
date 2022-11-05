#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def getSkyline(self, buildings):
        if not buildings:
            return []

        len_b = len(buildings)
        if len_b == 1:
            lx, rx, h = buildings[0]
            return [
                [lx, h],
                [rx, 0]
            ]

        mid = len_b // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return merge(left, right)


def merge(left, right):
    len_l = len(left)
    len_r = len(right)
    i = j = 0
    r = []
    lh = rh = None
    while i < len_l and j < len_r:
        lx = left[i][0]
        ly = left[i][1]
        rx = right[j][0]
        ry = right[j][1]
        if lx < rx:
            lh = ly
            new = [lx, max(lh, rh)]
            i += 1
        elif rx < lx:
            rh = ry
            new = [rx, max(lh, rh)]
            j += 1
        else:
            lh = ly
            rh = ry
            new = [lx, max(lh, rh)]
            i += 1
            j += 1

        if not r or r[-1][1] != new[1]:
            r.append(new)

    while i < len_l:
        if not r or r[-1][1] != left[i][1]:
            r.append(left[i])
        i += 1

    while j < len_r:
        if not r or r[-1][1] != right[j][1]:
            r.append(right[j])
        j += 1

    return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [
                [2, 9, 10],
                [3, 7, 15],
                [5, 12, 12],
                [15, 20, 10],
                [19, 24, 8]
            ],
            [
                [2, 10],
                [3, 15],
                [7, 12],
                [12, 0],
                [15, 10],
                [20, 8],
                [24, 0]
            ]
        ),
    ]
    f = s.getSkyline
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
