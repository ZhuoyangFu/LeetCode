# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not (list1 and list2):
            return list1 if list1 else list2

        if list1.val <= list2.val:
            list1.next = Solution().mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = Solution().mergeTwoLists(list1,list2.next)
            return list2