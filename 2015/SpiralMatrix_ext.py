#!/usr/bin/env python
# encoding: utf-8


def spiral_array(n, height, width):
    li = [0] * width
    m = [li[:] for i in range(height)]
    direction = 0
    x, y = -1, 0
    v = 1
    while height > 0 and width > 0:
        moves = height if direction % 2 else width
        for i in range(moves):
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1

            m[y][x] = v
            v += 1

        if direction % 2:
            width -= 1
        else:
            height -= 1

        direction = (direction + 1) % 4

    return m


if __name__ == '__main__':
    for li in spiral_array(20, 4, 5):
        print li
