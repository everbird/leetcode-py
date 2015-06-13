#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


def printl(n):
    if n:
        print n
        printl(n.next)


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return

        h = head
        if h.next:
            nh = self.reverseList(h.next)
            p = nh
            while p.next:
                p = p.next
            p.next = h
            h.next = None
            return nh
        else:
            return h


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    h = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    printl(h)
    nh = s.reverseList(h)
    print '-' * 6
    printl(nh)
