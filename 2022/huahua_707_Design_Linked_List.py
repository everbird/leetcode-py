#!/usr/bin/env python3

class ListNode:
    next = None

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "<ListNode: val={} next={}>".format(self.val, self.next)


class MyLinkedList:

    dummy = None

    def __init__(self):
        self.dummy = ListNode(None)


    def get(self, index: int) -> int:
        p = self.get_node(index)
        if not p:
            return -1

        return p.val


    def get_node(self, index: int) -> ListNode:
        p = self.dummy.next
        if not p:
            return

        for i in range(index):
            if p:
                p = p.next
            else:
                break

        return p


    def addAtHead(self, val: int) -> None:
        _next = self.dummy.next
        p = ListNode(val)
        self.dummy.next = p
        p.next = _next


    def addAtTail(self, val: int) -> None:
        pre = self.dummy
        p = self.dummy.next
        while p:
            pre = p
            p = p.next

        pre.next = ListNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        pre = self.get_node(index-1)
        if not pre:
            return

        _next = pre.next
        p = ListNode(val)
        pre.next = p
        p.next = _next


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            pre = self.dummy
        else:
            pre = self.get_node(index-1)

        if not pre:
            return

        p = pre.next
        if not p:
            return
        pre.next = p.next
        p.next = None
