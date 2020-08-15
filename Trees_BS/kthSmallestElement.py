# LC: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k): # n^2 soln
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # your k == how many nodes to the left of you or
        # if you're a right child, k of parent + 1
        # function to find how many children on left, thats you're count
        # if count == k, return
        # if count > k -> go left -> pass left node into kthSmallest, k = k
        # if count < k -> go right -> pass right node into kth smallest, k = k - count
        
        rootCount = self.kcount(root.left) + 1
        if rootCount > k:
            return self.kthSmallest(root.left, k)
        if rootCount < k:
            return self.kthSmallest(root.right, k - rootCount)
        return root.val # if rootCount == k:
        
    # count all nodes and children (pass left node into this)
    def kcount(self, node):
        # bfs to count
        if node == None: 
            return 0
        return self.kcount(node.left) + self.kcount(node.right) + 1


    def kthSmallestRecursive(self, root, k): # n space, n time
      return self.inOrder(root)[k-1]

    # return in order list
    def inOrder(self, root):
      if root == None:
        return []
      return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) 

    def kthSmallestStack(self, root, k): # (h + k) time, (h) space
      stack = []
      
      while(True):
        while root:
          stack.append(root)
          root = root.left
        root = stack.pop()
        k = k - 1
        if k == 0:
          return root.val
        root = root.right

        
    
def test():
  sol = Solution()

  #     3
  #   1  4
  #  _ 2
  testTree1 = TreeNode(3)
  testTree1.left = TreeNode(1)
  testTree1.left.right = TreeNode(2)
  testTree1.right = TreeNode(4)
  print(sol.kthSmallest(testTree1,1) == 1)
  print(sol.kthSmallest(testTree1,2) == 2)
  print(sol.kthSmallest(testTree1,3) == 3)
  print(sol.kthSmallest(testTree1,4) == 4)

  #     5
  #   3   6
  #  2 4
  # 1
  testTree2 = TreeNode(5)
  testTree2.right = TreeNode(6)
  testTree2.left = TreeNode(3)
  testTree2.left.left = TreeNode(2)
  testTree2.left.right = TreeNode(4)
  testTree2.left.left.left = TreeNode(1)
  print(sol.kthSmallest(testTree2,1) == 1)
  print(sol.kthSmallest(testTree2,2) == 2)
  print(sol.kthSmallest(testTree2,3) == 3)
  print(sol.kthSmallest(testTree2,4) == 4)
  print(sol.kthSmallest(testTree2,5) == 5)
  print(sol.kthSmallest(testTree2,6) == 6)

def testRecursive():
  sol = Solution()

  #     3
  #   1  4
  #  _ 2
  testTree1 = TreeNode(3)
  testTree1.left = TreeNode(1)
  testTree1.left.right = TreeNode(2)
  testTree1.right = TreeNode(4)
  print(sol.kthSmallestRecursive(testTree1,1) == 1)
  print(sol.kthSmallestRecursive(testTree1,2) == 2)
  print(sol.kthSmallestRecursive(testTree1,3) == 3)
  print(sol.kthSmallestRecursive(testTree1,4) == 4)

  #     5
  #   3   6
  #  2 4
  # 1
  testTree2 = TreeNode(5)
  testTree2.right = TreeNode(6)
  testTree2.left = TreeNode(3)
  testTree2.left.left = TreeNode(2)
  testTree2.left.right = TreeNode(4)
  testTree2.left.left.left = TreeNode(1)
  print(sol.kthSmallestRecursive(testTree2,1) == 1)
  print(sol.kthSmallestRecursive(testTree2,2) == 2)
  print(sol.kthSmallestRecursive(testTree2,3) == 3)
  print(sol.kthSmallestRecursive(testTree2,4) == 4)
  print(sol.kthSmallestRecursive(testTree2,5) == 5)
  print(sol.kthSmallestRecursive(testTree2,6) == 6)


def testStack():
  sol = Solution()

  #     3
  #   1  4
  #  _ 2
  testTree1 = TreeNode(3)
  testTree1.left = TreeNode(1)
  testTree1.left.right = TreeNode(2)
  testTree1.right = TreeNode(4)
  print(sol.kthSmallestStack(testTree1,1) == 1)
  print(sol.kthSmallestStack(testTree1,2) == 2)
  print(sol.kthSmallestStack(testTree1,3) == 3)
  print(sol.kthSmallestStack(testTree1,4) == 4)

  #     5
  #   3   6
  #  2 4
  # 1
  testTree2 = TreeNode(5)
  testTree2.right = TreeNode(6)
  testTree2.left = TreeNode(3)
  testTree2.left.left = TreeNode(2)
  testTree2.left.right = TreeNode(4)
  testTree2.left.left.left = TreeNode(1)
  print(sol.kthSmallestStack(testTree2,1) == 1)
  print(sol.kthSmallestStack(testTree2,2) == 2)
  print(sol.kthSmallestStack(testTree2,3) == 3)
  print(sol.kthSmallestStack(testTree2,4) == 4)
  print(sol.kthSmallestStack(testTree2,5) == 5)
  print(sol.kthSmallestStack(testTree2,6) == 6)


test()
testRecursive()
testStack()