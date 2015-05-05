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
        # n = L - (L - n)
        p = r = head
        for i in range(n):
            p = p.next

        if p is None:
            return r.next

        while p.next is not None:
            p = p.next
            r = r.next

        r.next = r.next.next
        return head


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
