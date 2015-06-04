#!/usr/bin/env python
# encoding: utf-8

d = {}


def cache(f):
    def _(inst, dp, index):
        r = d.get(index)
        if r is None:
            r = f(inst, dp, index)
            d[index] = r
        return r
    return _


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        lens = len(s)
        dp = [None] * (lens+1)
        for i in range(lens, -1, -1):
            v = []
            for j in range(i):
                if s[j:i] in wordDict:
                    v.append(s[j:i])
            dp[i] = v

        d.clear()
        r = self.dfs(dp, lens)
        return r

    @cache
    def dfs(self, dp, index):
        r = []
        ws = dp[index]
        for w in ws:
            i = index - len(w)
            if i == 0:
                r.append(w)
            else:
                vs = self.dfs(dp, i)
                for v in vs:
                    r.append(v+' '+w)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    print s.wordBreak('baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
