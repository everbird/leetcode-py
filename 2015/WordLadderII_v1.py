#!/usr/bin/env python
# encoding: utf-8


import string
import collections


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        bqueue = collections.deque([start])
        equeue = collections.deque([end])
        bs = {start}
        es = {end}
        wl = len(start)
        br = []
        er = []
        ledder = {}
        while bqueue and equeue:
            bl = len(bqueue)
            tbr = []
            for x in range(bl):
                w = bqueue.popleft()
                for i in range(wl):
                    for c in string.ascii_lowercase:
                        t = w[:i] + c + w[i+1:]
                        if t in es:
                            tbr.append(t)
                            br.append(tbr)
                            break
                        if t in dict and t not in bs:
                            bs.add(t)
                            bqueue.append(t)
                tbr.append(w)
            br.append(tbr)

            el = len(equeue)
            ter = []
            for x in range(el):
                w = equeue.popleft()
                for i in range(wl):
                    for c in string.ascii_lowercase:
                        t = w[:i] + c + w[i+1:]
                        if t in bs:
                            ter.append(t)
                            er.append(ter)
                            break
                        if t in dict and t not in es:
                            es.add(t)
                            equeue.append(t)
                ter.append(w)
            er.append(ter)

        return br, er


if __name__ == '__main__':
    s = Solution()
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
