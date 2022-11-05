#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):

    def findItinerary(self, tickets):
        d = defaultdict(list)
        for src, dest in tickets:
            d[src].append(dest)

        for v in d.values():
            v.sort()


        r = []

        def dfs(dd, src):
            r.append(src)

            next_nodes = dd[src]
            if all(not x for x in dd.values()):
                return True

            n = len(next_nodes)
            for i in xrange(n):
                next_node = next_nodes.pop(0)
                found = dfs(dd, next_node)
                if found:
                    return found
                next_nodes.append(next_node)

            x = r.pop()

        dfs(d, 'JFK')
        return r



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"]
        ),
        (
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            ["JFK","ATL","JFK","SFO","ATL","SFO"]
        ),
    ]
    f = s.findItinerary
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
