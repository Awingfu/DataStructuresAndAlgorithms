# https://leetcode.com/problems/validate-binary-search-tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Brute Force
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root == None:
#             return True

#         if self.left_valid(root.left, root.val) and self.right_valid(root.right, root.val):
#             return self.isValidBST(root.left) and self.isValidBST(root.right)
#         else:
#             return False

#     def left_valid(self, node, rootVal):
#         if node == None:
#             return True
#         if node.val < rootVal:
#             maxLeft = node
#             while maxLeft.right:
#                 maxLeft = maxLeft.right
#             return maxLeft.val < rootVal
#         return False

#     def right_valid(self, node, rootVal):
#         if node == None:
#             return True
#         if node.val > rootVal:
#             minRight = node
#             while minRight.left:
#                 minRight = minRight.left
#             return minRight.val > rootVal
#         return False

# Recursive
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.helper(root)
#     def helper(self, node, lower = float('-inf'), upper = float('inf')):
#         if node is None:
#             return True
        
#         val = node.val
#         if val <= lower or val >= upper:
#             return False
        
#         return self.helper(node.left, lower, val) and self.helper(node.right,val,upper)

# Iterative
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        stack = [(root,float('-inf'),float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))
        return True