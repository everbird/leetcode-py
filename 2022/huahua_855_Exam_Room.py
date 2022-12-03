#!/usr/bin/env python3

from collections import deque


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seated = []

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0

        # BFS
        q = deque([(x, 0) for x in sorted(self.seated)])
        visited = set()
        ri = -1
        rd = 0
        while q:
            i, d = q.popleft()
            if i < 0 or i >= self.n or i in visited:
                continue

            visited.add(i)

            if d > rd:
                rd = d
                ri = i

            # order matters
            q.append((i-1, d+1))
            q.append((i+1, d+1))

        if ri != -1:
            self.seated.append(ri)

        return ri

    def leave(self, p: int) -> None:
        if p in self.seated:
            self.seated.remove(p)

# TLE


from collections import deque
from bisect import bisect

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seated = []

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0

        if len(self.seated) == 1:
            if self.n-1 - self.seated[0] > self.seated[0]:
                self.seated.append(self.n-1)
                return self.n-1

            self.seated.insert(0, 0)
            return 0

        pre = None
        ri = -1
        d = 0
        if self.seated[0] > d:
            ri = 0
            d = self.seated[0]

        for p in self.seated:
            if pre is None:
                pre = p
                continue

            m = (p + pre) // 2
            if m != pre and min(m-pre, p-m) > d:
                d = min(m-pre, p-m)
                ri = m

            pre = p

        if self.n-1-self.seated[-1] > d:
            ri = self.n-1
            d = self.n-1-self.seated[-1]

        if ri != -1:
            index = bisect(self.seated, ri)
            self.seated.insert(index, ri)

        return ri

    def leave(self, p: int) -> None:
        self.seated.remove(p)

# TLE again

from collections import deque
from bisect import bisect

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seated = []

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0

        if len(self.seated) == 1:
            if self.n-1 - self.seated[0] > self.seated[0]:
                self.seated.append(self.n-1)
                return self.n-1

            self.seated.insert(0, 0)
            return 0

        pre = None
        ri = -1
        d = 0
        if self.seated[0] > d:
            ri = 0
            d = self.seated[0]

        for p in self.seated:
            if pre is None:
                pre = p
                continue

            m = (p + pre) // 2
            if m != pre and m-pre > d:
                d = m-pre
                ri = m

            pre = p

        if self.n-1-self.seated[-1] > d:
            ri = self.n-1
            d = self.n-1-self.seated[-1]

        if ri != -1:
            index = bisect(self.seated, ri)
            self.seated.insert(index, ri)

        return ri

    def leave(self, p: int) -> None:
        self.seated.remove(p)
