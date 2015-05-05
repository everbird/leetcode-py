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
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        head = p = ListNode(0)
        while l1 or l2:
            if not l2 or (l1 and l1.val < l2.val):
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next

            p = p.next

        return head.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(5)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(2)
    m2 = ListNode(6)
    m3 = ListNode(7)
    m1.next = m2
    m2.next = m3

    s = Solution()
    r = s.mergeTwoLists(n1, m1)
    print_l(r)
