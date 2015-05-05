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
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        rhead = reverseListNode(head)
        if n == 1:
            rhead = rhead.next

        p = None
        cur = rhead
        while n - 1 > 0:
            p = cur
            cur = cur.next
            n -= 1
        if p:
            p.next = cur.next
        return reverseListNode(rhead)


def reverseListNode(head):
    if not head:
        return None

    p = head
    head = head.next if head else None
    p.next = None
    while head:
        t = head.next
        head.next = p
        p = head
        head = t

    return p


if __name__ == '__main__':
    head = n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5


    s = Solution()
    r = s.removeNthFromEnd(head, 2)
    #r = reverseListNode(head)
    print_l(r)
