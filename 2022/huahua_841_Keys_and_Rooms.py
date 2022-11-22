#!/usr/bin/env python3

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        cnt = 0
        def dfs(x):
            nonlocal cnt
            keys = rooms[x]
            rooms[x] = None
            cnt += 1
            
            for k in keys:
                if rooms[k] is not None:
                    dfs(k)

        dfs(0)
        return cnt == n
