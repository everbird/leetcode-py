#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head

        pre = None
        h = head
        count = m
        while count > 1:
            pre = h
            h = h.next
            count -= 1

        p1 = pre
        p2 = h

        f = None
        b = None
        while n >= m:
            if f:
                h = f

            f = h.next

            if b:
                h.next = b

            b = h
            m += 1

        p4 = f
        p3 = h

        new_head = None
        if pre:
            pre.next = p3
            new_head = head
        else:
            new_head = p3

        if p2:
            p2.next = p4

        return new_head


if __name__ == '__main__':
    s = Solution()
    head = n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    h = s.reverseBetween(head, 2, 4)
    print_l(h)

    print '-' * 6

    head = n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    h = s.reverseBetween(head, 3, 4)
    print_l(h)
