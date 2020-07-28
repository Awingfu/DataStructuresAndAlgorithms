
class Node:
  def __init__(self, value, parent = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent
  
def twoSum(root, value):
  pointer = root
  my_dict = {}
  
  while !pointer.left:
    pointer = pointer.left

  while !pointer:
    




def test():
#build tree
    head = Node(5)
    head.left = Node(3, head)
    head.left.left = Node(2, head.left)
    head.left.right = Node(4, head.left)
    head.right = Node(7, head)
    head.right.left = Node(6, head.right)
    head.right.right = Node(8, head.right)
   #    5
   #  3   7
   # 2 4 6 8
   print(twoSum(head, 10))