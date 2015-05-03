#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        lr = c = None
        flag = False
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            r = a + b
            if flag:
                r += 1

            flag = bool(r / 10)
            node = ListNode(r % 10)
            # Record result list head
            if not lr:
                lr = node

            if c:
                c.next = node

            c = node

            l1 = l1.next
            l2 = l2.next

        return lr


def print_list(list_head):
    print_l(list_head)
    print '\n'


def print_l(list_head):
    if list_head:
        print list_head.val,
        print_l(list_head.next)


if __name__ == '__main__':
    l1a = ListNode(2)
    l1b = ListNode(4)
    l1c = ListNode(3)
    l1a.next = l1b
    l1b.next = l1c
    l1 = l1a

    l2a = ListNode(5)
    l2b = ListNode(6)
    l2c = ListNode(4)
    l2a.next = l2b
    l2b.next = l2c
    l2 = l2a

    s = Solution()
    lr = s.addTwoNumbers(l1, l2)
    print_list(l1)
    print_list(l2)
    print_list(lr)
