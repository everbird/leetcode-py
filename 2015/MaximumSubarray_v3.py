#!/usr/bin/env python
# encoding: utf-8


def max_subarrray(array):
    max_v = 0
    s = 0
    for n in array:
        s += n
        if s < 0:
            s = 0
        else:
            max_v = max(max_v, s)

    return max_v

if __name__ == '__main__':
    b = [-2,1,-3,4,-1,2,1,-5,4]
    print max_subarrray(b)
