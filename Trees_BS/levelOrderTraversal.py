# https://leetcode.com/problems/binary-tree-level-order-traversal
#  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     # breadth first search
    #     # initialize result = [[root.val]]
    #     # initialize queue = [root]
    #     # intiialize temp = []
    #     # while queue
    #     # initialize next_queue = []
    #     # for each node in queue
    #     # for each child in node
    #     # append child val to temp
    #     # append child to next_queue
    #     # result.append(temp)
    #     # temp = []
    #     # queue = next_queue
    #     if root is None:
    #         return []
    #     result = [[root.val]]
    #     queue = [root]
    #     temp = []
    #     while len(queue) > 0:
    #         next_queue = []
    #         for node in queue:
    #             if node.left:
    #                 next_queue.append(node.left)
    #                 temp.append(node.left.val)
    #             if node.right:
    #                 next_queue.append(node.right)
    #                 temp.append(node.right.val)
    #         if temp:
    #             result.append(temp)
    #             temp = []
    #         queue = next_queue
    #     return result
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # breadth first search
        # recusive
        levels = []
        if root is None:
            return []
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return result