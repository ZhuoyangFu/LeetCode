# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def judge(root):
            if not root:
                return 0
            left = judge(root.left)
            if left == -1:
                return -1
            right = judge(root.right)
            if right == -1:
                return -1

            return -1 if abs(left - right) > 1 else max(left, right) + 1

        return judge(root) >= 0