#!/usr/bin/env python
# -*- coding: utf-8 -*-


def run():
    input_data = [
            [2],
            [3,4],
            [6,5,7],
            [4,1,8,3],
            ]
    r = get_path(input_data, 0, 0)
    print r


def get_path(data, index, depth):
    if depth > len(data) - 1:
        return 0


    a, b = get_path(data, index, depth+1), get_path(data, index+1, depth+1)

    return min(a, b) + data[depth][index]



def main():
    run()


if __name__ == '__main__':
    main()
