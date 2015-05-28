#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if self.is_1diff(start, end):
            return [[start, end]]
        r = []
        indexes = self.find_1diff_indexes(start, dict)
        for i in indexes:
            p = dict[i]
            new_dict = dict[:i] + dict[i+1:]
            items = self.findLadders(p, end, new_dict)
            for item in items:
                if (len(item) > 1
                    and self.get_diff_index(start, item[0]) == self.get_diff_index(item[0], item[1])):
                    continue

                r.append([start]+item)
        return r

    def find_1diff_indexes(self, a, d):
        r = []
        for i in range(len(d)):
            if self.is_1diff(a, d[i]):
                r.append(i)
        return r

    def is_1diff(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1

    def get_diff_index(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return i


if __name__ == '__main__':
    s = Solution()
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
