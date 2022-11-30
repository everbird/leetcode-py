#!/usr/bin/env python3

from collections import defaultdict


class DisjointSet:

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
        elif self.ranks[py] > self.parents[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emap = {}
        eindices = []
        cnt = 0
        def _get_index(x):
            nonlocal cnt, emap, eindices
            if x in emap:
                return emap[x]

            emap[x] = cnt
            eindices.append(x)
            cnt += 1
            return emap[x]

        def _get_email(x):
            return eindices[x]

        u = DisjointSet(len(accounts)*10)
        email_to_names = {}
        for line in accounts:
            if len(line) == 1:
                continue

            name = line[0]
            first = line[1]
            email_to_names[first] = name
            for email in line[2:]:
                u.union(_get_index(first), _get_index(email))
                email_to_names[email] = name

        d = defaultdict(list)
        for email in email_to_names.keys():
            root_email_index = u.find(_get_index(email))
            root_email = _get_email(root_email_index)
            d[root_email].append(email)

        rs = []
        for root_email, emails in d.items():
            r = []
            name = email_to_names[root_email]
            r.append(name)
            r.extend(sorted(emails))
            rs.append(r)
        return rs


def n2cidr(ip, n):
    reserve = 32 - n
    n = ip2int(ip)
    decimals = []
    m = 3
    while reserve >= 8:
        mask = 256 ** m
        d = n // mask 
        decimals.append(d)
        n = n % mask
        m -= 1
        reserve -= 8

    k = 32
    if reserve > 0:
        k -= reserve
        decimals.append(n)

    return "{}/{}".format(
        ".".join(map(str, decimals)),
        k
    )
