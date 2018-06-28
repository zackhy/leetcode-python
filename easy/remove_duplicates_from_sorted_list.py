class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        tmp = head.next
        pointer = head

        while tmp:
            if tmp.val != pointer.val:
                pointer.next = tmp
                pointer = pointer.next
            else:
                pointer.next = None

            tmp = tmp.next

        return head
