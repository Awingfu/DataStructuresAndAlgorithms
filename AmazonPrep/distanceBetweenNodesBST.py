# https://leetcode.com/discuss/interview-question/376375/

def bstDistance(nums, node1, node2):
  # build bst
  root = buildBST(nums)
  # find lowest common ancestor
  lca = findLCA(root, node1, node2)
  # get distance from node1 to lca + distance from node2 to lca
  return getDistance(lca, node1) + getDistance(lca, node2)

def getDistance(lca, node):
  if lca.val == node:
    return 0
  elif lca.val < node:
    return 1 + getDistance(lca.right, node)
  else:
    return 1 + getDistance(lca.left, node)

def findLCA(root, node1, node2):
  while(True):
    if root.val > node1 and root.val > node2:
      root = root.left
    elif root.val < node1 and root.val < node2:
      root = root.right
    else:
      return root

def buildBST(nums):
  root = bstNode(nums[0])
  for num in nums[1:]:
    newNode = bstNode(num)
    root.addNode(newNode)
  return root

class bstNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def addNode(self, node):
    if node.val > self.val:
      # go right
      if self.right == None:
        self.right = node
      else:
        self.right.addNode(node)
    elif node.val < self.val:
      # go left
      if self.left == None:
        self.left = node
      else:
        self.left.addNode(node)
    

test1 = bstDistance([2,1,3], 1,3)
print(test1 == 2)