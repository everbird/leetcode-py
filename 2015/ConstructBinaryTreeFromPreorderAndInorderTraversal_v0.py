#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        leni = len(inorder)
        lenp = len(preorder)
        if leni == 0 or lenp == 0:
            return None

        if leni == 1:
            return TreeNode(inorder[0])

        index = 0
        while index < lenp and preorder[index] not in inorder:
            index += 1

        if index == lenp:
            return

        p = preorder[index]

        t = TreeNode(p)

        k = 0
        for i in range(leni):
            if inorder[i] == p:
                k = i
                break

        left = inorder[:k]
        right = inorder[k+1:]

        if not left and not right:
            return None

        leftn = self.buildTree(preorder[1:], left)
        if leftn:
            t.left = leftn

        rightn = self.buildTree(preorder[1:], right)
        if rightn:
            t.right = rightn

        return t

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return

        print root.val
        self.inorder(root.left)
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()
    h = s.buildTree([1,2,3,4,5], [2,1,4,3,5])
    s.inorder(h)
    print '-' * 6
    s.preorder(h)

    h = s.buildTree([], [])
