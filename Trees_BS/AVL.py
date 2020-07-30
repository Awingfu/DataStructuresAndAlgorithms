# based on MIT lectures
class AVLNode:
  def __init__(self, value, parent = None):
    self.parent = parent
    self.left = None
    self.right = None
    self.value = value
    self.height = 0

  def insert(self, node):
    if node is None:
      return
    if node.value < self.value:
      if self.left is None:
        node.parent = self
        self.left = node
      else:
        self.left.insert(node)
    else:
      if self.right is None:
        node.parent = self
        self.right = node
      else:
        self.right.insert(node)

  def _str(self):
    """Internal method for ASCII art."""
    label = str(self.value)
    if self.left is None:
      left_lines, left_pos, left_width = [], 0, 0
    else:
      left_lines, left_pos, left_width = self.left._str()
    if self.right is None:
      right_lines, right_pos, right_width = [], 0, 0
    else:
      right_lines, right_pos, right_width = self.right._str()
    middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
    pos = left_pos + middle // 2
    width = left_pos + middle + right_width - right_pos
    while len(left_lines) < len(right_lines):
      left_lines.append(' ' * left_width)
    while len(right_lines) < len(left_lines):
      right_lines.append(' ' * right_width)
    if (middle - len(label)) % 2 == 1 and self.parent is not None and \
      self is self.parent.left and len(label) < middle:
      label += '.'
    label = label.center(middle, '.')
    if label[0] == '.': label = ' ' + label[1:]
    if label[-1] == '.': label = label[:-1] + ' '
    lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
            ' ' * left_pos + '/' + ' ' * (middle-2) +
            '\\' + ' ' * (right_width - right_pos)] + \
      [left_line + ' ' * (width - left_width - right_width) + right_line
      for left_line, right_line in zip(left_lines, right_lines)]
    return lines, pos, width

  def __str__(self):
    return '\n'.join(self._str()[0])


def height(node):
  if node is None:
    return -1
  else:
    return node.height

def update_height(node):
  node.height = max(height(node.left), height(node.right)) + 1
 
class AVLTree:
  def __init__(self, root):
    self.root = root
  
  # move node x to the left and have right child become parent
  def left_rotate(self, x):
    # declare right child
    y = x.right
    print("rotating " + str(x.value) + " left")
    # re-assign parent of x to parent of y
    y.parent = x.parent
    if y.parent is None:
      self.root = y
    else:
      if y.parent.left is x:
        y.parent.left = y
      elif y.parent.right is x:
        y.parent.right = y
    # swap left child of y to right child of x
    x.right = y.left
    if x.right is not None:
      x.right.parent = x
    # reconnect x and y
    y.left = x
    x.parent = y
    # update height x
    update_height(x)
    # update height y (parent of x)
    update_height(y)

  def right_rotate(self, x):
    y = x.left
    print("rotating " + str(x.value) + " right")
    y.parent = x.parent
    if y.parent is None:
      self.root = y
    else:
      if y.parent.left is x:
        y.parent.left = y
      elif y.parent.right is x:
        y.parent.right = y
    # swap right child of y to left child of x
    x.left = y.right
    if x.left is not None:
      x.left.parent = x
    # reconnect x and y
    y.right = x
    x.parent = y
    update_height(x)
    update_height(y)

  def rebalance(self, node):
    while node is not None:
      update_height(node)
      # if left is heavier than right
      if height(node.left) >= 2 + height(node.right):
        # if left's left is greater than or equal to left's right
        if height(node.left.left) >= height(node.left.right):
          # right rotate node
          self.right_rotate(node)
        # else, left's left is less than left's right
        else:
          self.left_rotate(node.left)
          self.right_rotate(node)
      elif height(node.right) >= 2 + height(node.left):
        if height(node.right.right) >= height(node.right.left):
          self.left_rotate(node)
        else:
          self.right_rotate(node.right)
          self.left_rotate(node)
      node = node.parent

  def insert(self, node):
    self.root.insert(node)
    self.rebalance(node)

test = AVLNode(5)
testTree = AVLTree(test)
print(testTree.root)
print()
testTree.insert(AVLNode(4))
print(testTree.root)
print()
testTree.insert(AVLNode(3))
print(testTree.root)
print()
testTree.insert(AVLNode(2))
print(testTree.root)
print()
testTree.insert(AVLNode(1))
print(testTree.root)
print()
testTree.insert(AVLNode(0))
print(testTree.root)
print()
testTree.insert(AVLNode(6))
print(testTree.root)
print()
testTree.insert(AVLNode(10))
print(testTree.root)
print()
testTree.insert(AVLNode(12))
print(testTree.root)
print()
testTree.insert(AVLNode(14))
print(testTree.root)
print()
testTree.insert(AVLNode(16))
print(testTree.root)
print()