# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)
        a = 0

        while l1 and l2:
            s = l1.val + l2.val + a
            a = 1 if s >= 10 else 0
            l3.next = ListNode(s % 10)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        temp = l1 or l2

        while temp:
            s = temp.val + a
            a = 1 if s >= 10 else 0
            l3.next = ListNode(s % 10)
            temp = temp.next
            l3 = l3.next

        if a == 1:
            l3.next = ListNode(1)
            return head.next

        return head.next
