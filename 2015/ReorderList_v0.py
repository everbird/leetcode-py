#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


def printl(h):
    if h:
        print h.val
        printl(h.next)


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        _h = h = head
        while _h:
            p = None
            v = h
            while v.next:
                p = v
                v = v.next

            if p == h or p is None:
                break

            _h = h.next
            h.next = v
            p.next = None
            v.next = _h
            h = _h

        return head


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
    head = s.reorderList(h)
    printl(head)
