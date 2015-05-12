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
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return

        if not head.next:
            return head

        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1

        k %= l

        if k == 0:
            return head

        t = head
        for i in range(l - k - 1):
            t = t.next
        new_head = t.next
        t.next = None

        tail.next = head
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

    h = s.rotateRight(head, 5)
    print_l(h)
