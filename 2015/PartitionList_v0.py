#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        p = None
        ph = None
        h = head
        mid = None
        pre = None
        while h:
            if h.val < x:
                if not p:
                    p = h
                    ph = h
                else:
                    p.next = h
                    p = p.next

                if pre:
                    pre.next = h.next
            else:
                if not mid:
                    mid = h

                pre = h

            h = h.next

            if p:
                p.next = None

        if p:
            p.next = mid

        return ph or mid


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

    head = n1 = ListNode(1)
    h = s.partition(head, 0)
    print_l(h)
