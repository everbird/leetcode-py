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
    def sortList(self, head):
        if not head or not head.next:
            return head

        p1 = p2 = head
        pre = None
        while p1 and p2:
            pre = p1
            p1 = p1.next
            p2 = p2.next.next if p2.next else None

        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(p1)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        if not h1:
            return h2

        if not h2:
            return h1

        new_head = None
        p = None
        while h1 and h2:
            if h1.val < h2.val:
                if not new_head:
                    new_head = h1
                if p:
                    p.next = h1
                p = h1
                h1 = h1.next
            else:
                if not new_head:
                    new_head = h2
                if p:
                    p.next = h2
                p = h2
                h2 = h2.next

        if h1 and not h2:
            p.next = h1
        elif h2 and not h1:
            p.next = h2

        return new_head


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = ListNode(1)
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

    #n1, n2 = s.split(head)
    #print '-' * 6
    #printl(n1)
    #print '-' * 6
    #printl(n2)
    h = s.sortList(head)
    print '-' * 6
    printl(h)
