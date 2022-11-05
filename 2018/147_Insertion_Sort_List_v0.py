class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def print_l(head):
    if head:
        print head.val, '->', head

        if head.next:
            print_l(head.next)


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(None)
        dummy.next = head
        while head:
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # insert n after cur
            if cur.next != head:
                t = head.next
                head.next = cur.next
                cur.next = head

                pre.next = t
                head = t
            else:
                pre = head
                head = head.next
        return dummy.next

if __name__ == '__main__':
    head = n1 = ListNode(1)
    n2 = ListNode(1)
    n1.next = n2

    s = Solution()
    r = s.insertionSortList(head)
    print_l(r)

    print '-' * 5
    head = n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    r = s.insertionSortList(head)
    print_l(r)
