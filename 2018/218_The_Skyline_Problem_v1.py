#!/usr/bin/eni python
# encoding: utf-8


class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings:
            return []

        lenb = len(buildings)
        if lenb == 1:
            t = buildings[0]
            return [[t[0], t[2]], [t[1], 0]]

        mid = lenb // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        i = j = 0
        lenl = len(left)
        lenr = len(right)
        result = []
        hleft = None
        hright = None
        while i < lenl and j < lenr:
            if left[i][0] < right[j][0]:
                hleft = left[i][1]
                new = [left[i][0], max(hleft, hright)]
                if not result or result[-1][1] != new[1]:
                    result.append(new)
                i += 1
            elif left[i][0] > right[j][0]:
                hright = right[j][1]
                new = [right[j][0], max(hleft, hright)]
                if not result or result[-1][1] != new[1]:
                    result.append(new)
                j += 1
            else:
                hleft = left[i][1]
                hright = right[j][1]
                new = [left[i][0], max(hleft, hright)]
                if not result or result[-1][1] != new[1]:
                    result.append(new)
                i += 1
                j += 1

        while i < lenl:
            new = left[i]
            if not result or result[-1][1] != new[1]:
                result.append(new)
            i += 1

        while j < lenr:
            new = right[j]
            if not result or result[-1][1] != new[1]:
                result.append(new)
            j += 1

        return result


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
