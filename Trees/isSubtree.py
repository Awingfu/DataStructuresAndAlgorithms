# LC: https://leetcode.com/problems/subtree-of-another-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, s, t): # O(s_n^2)
        sList = self.inOrder(s) # O(s_n)
        for node in sList: # O(s_n)
          if node.val == t.val: 
            if self.sameTree(node, t): 
              return True
        return False

    def sameTree(self, s, t): # O(s_n + t_n)
        sList = list(map(lambda x: x.val, self.inOrder(s))) # O(s_n)
        tList = list(map(lambda x: x.val, self.inOrder(t))) # O(t_n)
        # print(sList)
        # print(tList)
        return sList == tList
        
    def inOrder(self, root):
        if root == None:
            return []
        return self.inOrder(root.left) + [root] + self.inOrder(root.right) 

    def isSubtreeUnique(self, s, t): # only works for unique node vals
        # if s.val != t.val: find matching root node is s
        # return isSubtree(matching node in s, t)
        # else matching root vals
        # traversal of each, compare lists vals
        if s.val != t.val:
          sList = self.inOrder(s)
          for node in sList:
            if node.val == t.val:
              print('test')
              if self.isSubtreeUnique(node, t): 
                return True
          return False

        sList = list(map(lambda x: x.val, self.inOrder(s)))
        tList = list(map(lambda x: x.val, self.inOrder(t)))
        # print(sList)
        # print(tList)
        return sList == tList

        

def test():
  sol = Solution()

  #    3
  #  4  5
  # 1 2
  testTree1 = TreeNode(3)
  testTree1.left = TreeNode(4)
  testTree1.right = TreeNode(5)
  testTree1.left.left = TreeNode(1)
  testTree1.left.right = TreeNode(2)

  #  4
  # 1 2
  testTree2 = TreeNode(4)
  testTree2.left = TreeNode(1)
  testTree2.right = TreeNode(2)
  print(sol.isSubtree(testTree1, testTree2))

  #        3
  #     4     5
  #  1    2
  # _ _  0  _
  testTree3 = TreeNode(3)
  testTree3.left = TreeNode(4)
  testTree3.right = TreeNode(5)
  testTree3.left.left = TreeNode(1)
  testTree3.left.right = TreeNode(2)
  testTree3.left.right.left = TreeNode(0)
  print(sol.isSubtree(testTree3, testTree2) == False)

  #        3
  #     4     5
  #   1   2
  # 0 _
  testTree4 = TreeNode(3)
  testTree4.left = TreeNode(4)
  testTree4.right = TreeNode(5)
  testTree4.left.left = TreeNode(1)
  testTree4.left.right = TreeNode(2)
  testTree4.left.left.left = TreeNode(0)

  print(sol.isSubtree(testTree4, testTree2) == False)

  #  1
  # 1 _
  testTree5 = TreeNode(1)
  testTree5.left = TreeNode(1)

  print(sol.isSubtree(testTree5, TreeNode(1)))







test()