# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return max(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        else:
            return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
