# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd_h = head
        mark = even_h = head.next
        if not even_h:
            return head

        while even_h and even_h.next:
            if even_h.next:
                odd_h.next = even_h.next
                odd_h = even_h.next

            even_h.next = odd_h.next
            even_h = odd_h.next

        odd_h.next = mark
        return head
