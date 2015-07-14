#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        s = []
        pre = None
        h = root
        while h or s:
            if h.left:
                t = h.left
                h.left = None
                s.append(h)
                h = t
            else:
                if pre is None or pre < h.val:
                    pre = h.val
                else:
                    return False

                if h.right:
                    h = h.right
                elif s:
                    h = s.pop()
                else:
                    break

        return True


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    root = n1
    n1.right = n2
    n2.left = n3

    print s.isValidBST(root)

    print '-'*6

    n1 = TreeNode(0)

    root = n1

    print s.isValidBST(root)

    print '-'*6

    n1 = TreeNode(1)
    n2 = TreeNode(1)

    root = n1
    n1.left = n2

    print s.isValidBST(root)
