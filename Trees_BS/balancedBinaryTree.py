#LC: https://leetcode.com/problems/balanced-binary-tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # def isBalanced(self, root):
    #     # find max heights on each side, compare distances from root, if max difference < 2, good
    #     if root == None:
    #         return True
        
    #     if abs(self.determineHeight(root.left, 0) - self.determineHeight(root.right, 0)) > 1:
    #       return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
            
    # def determineHeight(self, node, depth):
    #     if node == None:
    #         return depth
        
    #     return max(self.determineHeight(node.left, depth+1), self.determineHeight(node.right,depth+1))

    def isBalanced(self, root):
        if not root: 
            return True
        
        return self.checkBalance(root) != -1

    def checkBalance(self, node): 
        if not node:
            return 0
            
        leftHeight = self.checkBalance(node.left)
        rightHeight = self.checkBalance(node.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) < 2:
            return max(leftHeight, rightHeight) + 1
        
        return -1


def test():
  sol = Solution()
  # [1,2,2,3,null,null,3,4,null,null,4]
  #          1
  #      2       2
  #    3   _   _   3
  #  4  _         _  4
  # false
  temp = TreeNode(1)
  temp.left = TreeNode(2)
  temp.left.left = TreeNode(3)
  temp.left.left.left = TreeNode(4)
  temp.right = TreeNode(2)
  temp.right.right = TreeNode(3)
  temp.right.right.right = TreeNode(4)
  print(sol.isBalanced(temp) == False)

  # [3,9,20,null,null,15,7]
  #        3
  #    9       20 
  #  _  _    15   7
  # true
  temp2 = TreeNode(3)
  temp2.left = TreeNode(9)
  temp2.right = TreeNode(20)
  temp2.right.left = TreeNode(15)
  temp2.right.right = TreeNode(7)
  print(sol.isBalanced(temp2))

test()