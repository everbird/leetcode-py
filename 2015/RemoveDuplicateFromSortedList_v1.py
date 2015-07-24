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
    # @return {ListNode}
    def deleteDuplicates(self, head):
        p = None
        n = head
        while n:

            if p and p.val == n.val:
                p.next = n.next
            else:
                p = n

            n = n.next

        return head


if __name__ == '__main__':
    s = Solution()
    head = n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(4)
    n7 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    h = s.deleteDuplicates(head)
    print_l(h)

    print '-' * 9
    head = n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(1)
    n4 = ListNode(2)
    n5 = ListNode(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    h = s.deleteDuplicates(head)
    print_l(h)

    print '-' * 9
    head = n1 = ListNode(1)

    h = s.deleteDuplicates(head)
    print_l(h)

    print '-' * 9
    head = n1 = ListNode(1)
    n2 = ListNode(1)

    n1.next = n2

    h = s.deleteDuplicates(head)
    print_l(h)
