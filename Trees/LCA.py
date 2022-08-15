# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution assuming just binary tree
class Solution:
    def __init__(self):
        self.cache = {}
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        isPLeft = self.isValInTree(root.left, p.val)
        isPRight = self.isValInTree(root.right, p.val)
        isQLeft = self.isValInTree(root.left, q.val)
        isQRight = self.isValInTree(root.right, q.val)
        print(isPLeft, isPRight, isQLeft, isQRight)
        if isPLeft and isQLeft:
            print('check left')
            return self.lowestCommonAncestor(root.left, p, q)
        if isPRight and isQRight:
            print('check right')
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
        
    def isValInTree(self, root, val):
        if root is None:
            return False
        # print(root.val, val)
        if (root, val) in self.cache:
            return self.cache[(root,val)]
        if root.val == val:
            self.cache[(root,val)] = True
            return True
        result = self.isValInTree(root.left, val) or self.isValInTree(root.right, val)
        self.cache[(root, val)] = result
        return result