#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<ListNode val={}>'.format(self.val)


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
        pre = None
        new_head = None
        while head:
            _head, _next = reverse(head, k)
            if not new_head:
                new_head = _head
            if pre:
                pre.next = _head
            pre = head
            head = _next
        return new_head

def reverse(head, k):
    if k == 1:
        return head, None

    b = head
    for i in range(k-1):
        if b is None:
            return head, None
        b = b.next

    if b is None:
        return head, None

    a = head
    new_head = b
    _next = b.next
    pre = None
    for i in range(k):
        t = a
        a = a.next
        t.next = pre
        pre = t
    return new_head, _next


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

    print '------'
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
    r = s.reverseKGroup(head, 3)
    print_l(r)
