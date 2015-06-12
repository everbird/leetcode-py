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
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        p = head
        pre = None
        while p:
            if p.val == val:
                if pre:
                    pre.next = p.next
                else:
                    head = p.next
            else:
                pre = p

            p = p.next

        return head

if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(6)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)

    h = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    printl(h)
    nh = s.removeElements(h, 6)
    print '-' * 6
    printl(nh)

    print '===' * 3
    n1 = ListNode(1)
    n2 = ListNode(1)
    n1.next = n2
    h = n1
    printl(h)
    nh = s.removeElements(h, 1)
    print '-' * 6
    printl(nh)
