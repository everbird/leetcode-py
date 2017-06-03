#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        area = 0
        len_h = len(height)
        highest_i = find_max_i(height)
        left = height[:highest_i]
        right = height[highest_i+1:]
        return caculate_right_all(right) + caculate_right_all(list(reversed(left)))


def caculate_right_all(height):
    area = 0
    index = 0
    while height:
        area += caculate_right(height)
        index = find_max_i(height)
        height = height[index+1:]
    return area


def caculate_right(height):
    highest_i = find_max_i(height)
    if highest_i == 0:
        return 0

    all_area = (highest_i+1) * height[highest_i]
    black_area = sum(height[:highest_i+1])
    return all_area - black_area



def find_max_i(height):
    r = 0
    max_n = None
    for i, n in enumerate(height):
        if max_n is None or n > max_n:
            r = i
            max_n = n
    return r


if __name__ == '__main__':
    s = Solution()
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    print s.trap(a)

    #a = [1,2,1]
    #print s.trap(a)
    #a = [1,2,1,2,3]
    #print s._trap(a)

    a = [9,6,8,8,5,6,3]
    print s.trap(a)
