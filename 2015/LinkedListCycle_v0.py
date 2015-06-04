#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p2 = p1 = head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next.next if p2.next else None
            if p1 and p2 and p1 == p2:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n4

    print s.hasCycle(head)

    n1 = ListNode(1)
    head = n1
    print s.hasCycle(head)
