# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        dummy= result
        carrydigit = 0

        while l1 or l2:
            val = carrydigit
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carrydigit = val / 10
            val = val % 10

            dummy.next = ListNode(val)
            dummy = dummy.next

        if carrydigit == 1:
            dummy.next = ListNode(1)

        return result.next