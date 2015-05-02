#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pascals_triangle(k):
    result = []
    for i in range(k):
        _ = []
        if i == 0:
            _ = [1]
        else:
            for j in range(i+1):
                x = get_value(result, j-1) + get_value(result, j)
                _.append(x)
        result = _

    return result


def get_value(line, index):
    if index < 0 or index > len(line) - 1:
        return 0

    return line[index]


def run():
    r = pascals_triangle(5)
    print r

def main():
    run()

if __name__ == '__main__':
    main()
