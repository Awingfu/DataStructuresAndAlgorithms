# LC: https://leetcode.com/problems/validate-binary-search-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        if self.left_valid(root.left, root.val) and self.right_valid(root.right, root.val):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False

    def left_valid(self, node, rootVal):
        if node == None:
            return True
        if node.val < rootVal:
            maxLeft = node
            while maxLeft.right:
                maxLeft = maxLeft.right
            return maxLeft.val < rootVal
        return False

    def right_valid(self, node, rootVal):
        if node == None:
            return True
        if node.val > rootVal:
            minRight = node
            while minRight.left:
                minRight = minRight.left
            return minRight.val > rootVal
        return False

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
  print(sol.isValidBST(temp) == False)

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
  print(sol.isValidBST(temp2) == False)

  # [10,5,15,null,null,6,20]
  #          10
  #      5       15 
  #            6    20
  temp3 = TreeNode(10)
  temp3.left = TreeNode(5)
  temp3.right = TreeNode(15)
  temp3.right.left = TreeNode(6)
  temp3.right.right = TreeNode(20)
  print(sol.isValidBST(temp3) == False)

test()