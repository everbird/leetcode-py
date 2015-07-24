#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


def print_l(head):
    if head:
        print head.val

        if head.next:
            print_l(head.next)


class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        r = rt = ListNode(0)
        r.next = head
        n = head
        pre = None
        while n:
            _next = n.next
            if n.val < x:
                if pre:
                    pre.next = n.next
                    n.next = rt.next
                    rt.next = n
                rt = n
            else:
                pre = n
            n = _next

        return r.next


if __name__ == '__main__':
    s = Solution()
    head = n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    h = s.partition(head, 3)
    print_l(h)

    print '------'

    head = n1 = ListNode(1)
    h = s.partition(head, 0)
    print_l(h)

    print '------'

    head = n1 = ListNode(3)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3
    h = s.partition(head, 3)
    print_l(h)
