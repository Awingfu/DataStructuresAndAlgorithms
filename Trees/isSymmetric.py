# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.isMirror(root,root)

#     def isMirror(self, left, right):
#         if left is None and right is None:
#             return True
#         if left is None or right is None:
#             return False
#         return left.val == right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)

# iterative
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        nodeQ = deque()
        nodeQ.append(root.left)
        nodeQ.append(root.right)
        while nodeQ:
            left = nodeQ.popleft()
            right = nodeQ.popleft()
            if left == None and right == None: 
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            nodeQ.append(left.right)
            nodeQ.append(right.left)
            nodeQ.append(left.left)
            nodeQ.append(right.right)

        return True


test1 = TreeNode(0,TreeNode(1),TreeNode(1))
test2 = TreeNode(0,TreeNode(1, TreeNode(2)),TreeNode(1, None, TreeNode(2)))
test3 = TreeNode(0,TreeNode(1, TreeNode(2)),TreeNode(1, TreeNode(2)))

sol = Solution()
print(sol.isSymmetric(test1)) # true
print(sol.isSymmetric(test2)) # true
print(sol.isSymmetric(test3)) # false