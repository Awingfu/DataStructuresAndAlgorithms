class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

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

def sortedArrayToBST(nums):
  """
  :type nums: List[int]
  :rtype: TreeNode
  """
  def helper(arr, left, right):
    if left > right:
      return None
    mid = (right + left)//2
    new_node = TreeNode(arr[mid])
    new_node.left = helper(arr, left, mid-1)
    new_node.right = helper(arr, mid+1, right)
    return new_node

  return helper(nums, 0, len(nums)-1)

def sortedListToBST(head):
  """
  :type head: ListNode
  :rtype: TreeNode
  """
  value_arr = []
  n = head
  while (n != None):
    value_arr.append(n.val)
    n = n.next
  
  def helper(arr, left, right):
    if left > right: 
      return None
    mid = (right + left) // 2
    new_node = TreeNode(arr[mid])
    new_node.left = helper(arr, left, mid-1)
    new_node.right = helper(arr, mid+1, right)
    return new_node
      
  return helper(value_arr, 0, len(value_arr)-1)


def testArrayToBST():
  testArray = [-10, -3, 0, 5, 9]
  test = sortedArrayToBST(testArray)
  test.display()

def testListToBST():
  head = ListNode(-10)
  head.next = ListNode(-3)
  head.next.next = ListNode(0)
  head.next.next.next = ListNode(5)
  head.next.next.next.next = ListNode(9)
  bst_head = sortedListToBST(head)
  bst_head.display()

testArrayToBST()
testListToBST()