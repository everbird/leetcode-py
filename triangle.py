#!/usr/bin/env python
# -*- coding: utf-8 -*-


def run():
    #input_data = [
    #        [2],
    #        [3,4],
    #        [6,5,7],
    #        [4,1,8,3],
    #        ]

    input_data = [
            [-1],
            [2,3],
            [1,-1,-3]
            ]
    r = get_path(input_data)
    assert r==-1, 'Failed'
    print r


def get_path(data):
    d = [[0] * len(data) for i in data]
    last_line = data[-1]
    d[-1] = last_line

    get_min_sum(data, d, len(data) - 1)

    print d
    return d[0][0]


def get_min_sum(data, d, depth):
    print d
    if depth < 0:
        return

    if depth == len(data) - 1:
        d[depth] = data[depth]
    elif depth < len(data) - 1:
        next_line = d[depth + 1] # ! d, not data
        curret_line = data[depth]
        for i in range(len(curret_line)):
            a = next_line[i]
            b = next_line[i + 1]
            _i = i
            if a > b:
                _i = i + 1

            d[depth][i] = data[depth][i] + d[depth + 1][_i]
            print '>>>', data[depth][i], d[depth+1][_i], _i, a, b

    if depth > 0:
        get_min_sum(data, d, depth-1)



def main():
    run()


if __name__ == '__main__':
    main()
