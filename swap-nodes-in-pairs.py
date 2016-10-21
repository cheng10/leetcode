# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        res = dummy
        while res.next and res.next.next:
            tmp = res.next.next
            res.next.next = tmp.next
            tmp.next = res.next
            res.next = tmp
            res = res.next.next
        return dummy.next
