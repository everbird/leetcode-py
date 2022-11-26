#!/usr/bin/env python3

from collections import Counter, deque


class HitCounter:
    TTL = 5*60

    def __init__(self):
        self.q = deque()
        self.c = Counter()

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1] != timestamp:
            self.q.append(timestamp)

        self.c[timestamp] += 1

        self.refresh(timestamp)
        
    def refresh(self, timestamp):
        while self.q and self.q[0] < (timestamp - self.TTL):
            t = self.q.popleft()
            del self.c[t]

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for k,v in self.c.items():
            if timestamp-self.TTL < k <= timestamp:
                cnt += v
        return cnt


# deque with t, cnt pair should be enough
