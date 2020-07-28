
class Node:
  def __init__(self, value, parent = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent

# key is value - node.value, value is node
my_dict = {}
  
def twoSum(root, value):
  if root == None:
    return None
  
  check_left = twoSum(root.left, value)
  if check_left: 
    return check_left

  if root.value in my_dict.keys():
    return (root, my_dict[root.value])
  
  check_right = twoSum(root.right, value)
  if check_right:
    return check_right
  
  my_dict[value-root.value] = root
  return None




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
  x1, x2 = twoSum(head, 10)
  print(x1.value, x2.value)

test()