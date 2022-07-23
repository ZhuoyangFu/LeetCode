#Method 1 - Time Limit Exceed
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        l_less = []
        l_great = []

        p = head
        while p:
            if p.val < x:
                l_less.append(p.val)
            else:
                l_great.append(p.val)

        p = head

        for i in l_less:
            p.val = i
            p = p.next

        for i in l_great:
            p.val = i
            p = p.next

        return head

#Method 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        large = ListNode(0)
        small_root, large_root = small, large
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            temp = head.next
            head.next = None
            head = temp
        small.next  = large_root.next
        return small_root.next