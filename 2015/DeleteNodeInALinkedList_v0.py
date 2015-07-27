#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printl(root):
    if root:
        print root.val,
        printl(root.next)
    else:
        print


class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        pre = None
        h = node
        while h.next:
            h.val = h.next.val
            pre = h
            h = h.next

        pre.next = None


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    root = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    printl(root)
    print '-'*6
    s.deleteNode(n3)
    printl(root)
