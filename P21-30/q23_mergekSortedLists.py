# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        return self.merge(lists, 0, len(lists)-1)

    def mergeTwoLists(self, list1, list2):

        if not (list1 and list2):
            return list1 if list1 else list2

        if list1.val <= list2.val:
            list1.next = Solution().mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = Solution().mergeTwoLists(list1,list2.next)
            return list2

    def merge(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge(lists, start, mid)
        right = self.merge(lists, mid + 1, end)

        return self.mergeTwoLists(left, right)