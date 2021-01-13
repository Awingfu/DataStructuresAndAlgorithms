#https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
class Solution(object):
    max_path = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathFinder(root)
        return self.max_path
    
    def maxPathFinder(self, node):
        if node is None:
                return 0
        right_max_path = self.maxPathFinder(node.right)
        left_max_path = self.maxPathFinder(node.right)

        current_max_path = node.val + left_max_path + right_max_path
        self.max_path = max(current_max_path, self.max_path)

        return node.val + max(left_max_path,right_max_path)