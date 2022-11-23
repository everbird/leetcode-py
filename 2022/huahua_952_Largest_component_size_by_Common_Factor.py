#!/usr/bin/env python3

from collections import Counter


class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        lenn = len(nums)
        u = UnionFindSet(lenn)
        for j in range(lenn):
            for i in range(j+1, lenn):
                if gcd(nums[i], nums[j]) > 1:
                    u.union(i, j)

        c = Counter([u.find(i) for i in range(lenn)])
        return c.most_common(1)[0][1]


def gcd(x, y):
    if y == 0:
        return abs(x)

    return gcd(y, x % y)

#TLE
#Below is faster
#

rom collections import Counter


class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n+1))
        self.ranks = [0] * (n+1)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        lenn = len(nums)
        u = UnionFindSet(max(nums))
        for n in nums:
            for i in range(2, int(sqrt(n)+1)):
                if n % i == 0:
                    u.union(n, i)
                    u.union(n, n // i)

        c = Counter([u.find(nums[i]) for i in range(lenn)])
        return c.most_common(1)[0][1]
