#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


def printl(h):
    if h:
        print h
        printl(h.next)

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return head

        helper = ListNode(0)
        cur = head
        pre = helper
        next = None
        while cur:
            next = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next

            cur.next = pre.next
            pre.next = cur

            # Reset
            pre = helper

            cur = next

        return helper.next


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(5)
    n3 = ListNode(2)
    n4 = ListNode(4)
    n5 = ListNode(3)
    n6 = ListNode(6)

    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    #n5.next = n6

    printl(head)
    h = s.insertionSortList(head)
    print '-' * 6
    printl(h)
