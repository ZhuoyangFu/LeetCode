# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def Inorder(root):
            if not root:
                return
            Inorder(root.left)
            result.append(root.val)
            Inorder(root.right)

        Inorder(root)
        return result