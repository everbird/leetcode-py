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
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB

        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

        p = t = x = None
        if p1 and not p2:
            p = p1
            t = headB
            x = headA
        elif p2 and not p1:
            p = p2
            t = headA
            x = headB

        while p:
            p = p.next
            x = x.next

        while x and t and x != t:
            x = x.next
            t = t.next

        return x


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)

    m1 = ListNode(4)
    m2 = ListNode(5)
    m3 = ListNode(6)

    a1 = ListNode(9)
    a2 = ListNode(10)
    a3 = ListNode(11)

    h1 = n1
    n1.next = n2
    n2.next = a1
    h2 = m1
    m1.next = m2
    m2.next = m3
    m3.next = a1
    a1.next = a2
    a2.next = a3

    print s.getIntersectionNode(h1, h2)

    n1 = ListNode(1)
    n2 = ListNode(2)

    m1 = ListNode(4)
    m2 = ListNode(5)
    m3 = ListNode(6)


    h1 = n1
    n1.next = n2

    h2 = m1
    m1.next = m2
    m2.next = m3

    print s.getIntersectionNode(h1, h2)

    n1 = ListNode(1)
    h1 = h2 = n1
    print s.getIntersectionNode(h1, h2)
