#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def canVisitAllRooms(self, rooms):
        len_n = len(rooms)
        visited = [False] * len_n

        dfs_visit(0, rooms, visited)
        return all(visited)


def dfs_visit(index, rooms, visited):
    visited[index] = True
    keys = rooms[index]
    for key in keys:
        if visited[key]:
            continue
        dfs_visit(key, rooms, visited)


def main():
    s = Solution()
    tests = [
        (
            [[1],[2],[3],[]],
            True
        ),
        (
            [[1,3],[3,0,1],[2],[0]],
            False
        ),
    ]
    for input_args, expected in tests:
        r = s.canVisitAllRooms(input_args)
        print 'Input:{}\tOutput:{}\tExpected:{}'.format(input_args, r, expected)


if __name__ == '__main__':
    main()
