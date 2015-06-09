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
        print h
        printl(h.next)

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        new_head = None
        p = head
        while p:
            s = head
            pre = None
            while s.val < p.val and s != p:
                pre = s
                s = s.next

            _p = p.next

            if pre is None:
                new_head = p
            elif s != p:
                pre.next = p
                p.next = s
                # Find last sorted
                while s.next and s.next != p:
                    s = s.next
                s.next = _p

            p = _p

        return new_head


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(5)
    n3 = ListNode(2)
    n4 = ListNode(4)
    n5 = ListNode(3)
    n6 = ListNode(6)

    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    printl(head)
    h = s.insertionSortList(head)
    print '-' * 6
    printl(h)
