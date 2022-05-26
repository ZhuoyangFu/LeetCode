# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(-1)
        tail = pre

        q = head
        while q is not None:

            n = k
            p = q
            while p is not None and n > 0:
                p = p.next
                n -= 1

            if n > 0:
                tail.next = q
                break

            end = q
            while q != p:
                t = q.next
                q.next = tail.next
                tail.next = q
                q = t
            tail = end
        return pre.next