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
    def reverseKGroup(self, head, k):
        def enough(h):
            pre = p = h
            for i in range(k):
                if p is None:
                    return False, h, None
                pre = p
                p = p.next

            return True, h, pre

        def reverse(head):
            if not head:
                return None

            p = head
            pre = None
            for i in range(k):
                t = p.next
                p.next = pre
                pre = p
                p = t

            return pre, head

        r = p = ListNode(0)
        while True:
            f, head, b = enough(head)
            if not f:
                break

            c = b.next if b else None
            p.next = b
            p = head

            reverse(head)
            head.next = c

            head = c

        p.next = head
        return r.next




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
    r = s.reverseKGroup(head, 2)
    print_l(r)
