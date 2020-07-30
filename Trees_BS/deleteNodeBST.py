class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def display(self):
    lines, _, _, _ = self._display_aux()
    for line in lines:
      print(line)

  # taken off https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370
  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.val
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle

    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.val
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.val
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def deleteNode(root, key):
  """
  :type root: TreeNode
  :type key: int
  :rtype: TreeNode
  """
  if root == None:
    return root
  
  if root.val > key:
    root.left = deleteNode(root.left, key)
  elif root.val < key:
    root.right = deleteNode(root.right, key)
  else:
    if root.left == None and root.right == None:
      return None
    # only a left side, find predecessor then delete predecessor
    # replace root with next lowest value
    elif root.right == None:
      node = root.left
      while node.right:
          node = node.right
      root.val = node.val
      root.left = deleteNode(root.left, root.val)
    # right side or both sides, find successor then delete successor
    # basically replace root with the next highest value
    else:
      node = root.right
      while node.left:
          node = node.left
      root.val = node.val
      root.right = deleteNode(root.right, root.val)

  return root

def test():
  head = TreeNode(5)
  head.left = TreeNode(3)
  head.right = TreeNode(6)
  head.left.left = TreeNode(2)
  head.left.right = TreeNode(4)
  head.right.right = TreeNode(7)
  #       5
  #    3     6
  # 2   4       7
  head.display()

  head = deleteNode(head, 3)
  head.display()

test()