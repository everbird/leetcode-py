#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        p1 = p2 = head
        while p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next.next if p2.next else None
            if p1 == p2:
                break

        if p1 is None or p2 is None:
            return

        p = head
        while p != p1:
            p = p.next
            p1 = p1.next

        return p


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3

    print s.detectCycle(head)
