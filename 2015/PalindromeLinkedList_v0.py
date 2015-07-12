#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        p1 = p2 = head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next.next if p2.next else None

        rhead = p1
        rhead = self.reverse(rhead)
        while head and rhead and head.val == rhead.val:
            head = head.next
            rhead = rhead.next

        return bool(not rhead)

    def reverse(self, head):
        pre = None
        while head:
            pre, pre.next, head = head, pre, head.next
            #t = head.next
            #head.next = pre
            #pre = head
            #head = t

        return pre


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(1)

    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print s.isPalindrome(head)

    print '-' * 6
    n1 = ListNode(1)
    n2 = ListNode(2)

    head = n1
    n1.next = n2
    print s.isPalindrome(head)
