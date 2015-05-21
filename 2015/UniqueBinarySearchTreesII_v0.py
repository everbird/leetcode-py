#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self._make(1, n)

    def _make(self, start, end):
        r = []
        if start > end:
            return [None]

        for i in range(start, end+1):
            left = self._make(start, i-1)
            right = self._make(i+1, end)

            for li in left:
                for ri in right:
                    t = TreeNode(i)
                    t.left = li
                    t.right = ri
                    r.append(t)

        return r

if __name__ == '__main__':
    s = Solution()
    print s.generateTrees(3)
