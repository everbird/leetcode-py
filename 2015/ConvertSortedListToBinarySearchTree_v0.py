#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next

        return self._do(nodes)

    def _do(self, nodes):
        if not nodes:
            return

        lenn = len(nodes)
        b = 0
        e = lenn - 1
        mid = (b+e) // 2
        n = TreeNode(nodes[mid].val)
        n.left = self._do(nodes[:mid])
        n.right = self._do(nodes[mid+1:])
        return n


    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n8 = ListNode(8)

    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8

    h = s.sortedListToBST(head)
    s.inorder(h)
