# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.subTree(root.left, root.right)

    def subTree(self, left, right):
        if left is None and right is None:
            return True
        if left and right and left.val == right.val:
            return self.subTree(left.left, right.right) and self.subTree(left.right, right.left)
        else:
            return False
