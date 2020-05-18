class Node: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = 0 # 0 for black, 1 for red

    def colorTranslate(self):
        if self.color == 0:
            return('b')
        else:
            return('r')

    # taken off https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370
    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    # taken off https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val + self.colorTranslate()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val + self.colorTranslate()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val + self.colorTranslate()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val + self.colorTranslate()
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


class rbTree: 
    def __init__(self):
        self.root = Node(1)
        # Change rest to insertion operations
        self.root.left = Node(2)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right = Node(3)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.right.right.right = Node(15)
    
    def is_red_black_tree(self):
        if self.root = None:
            return True
        
        if self.root.color == 1:
            return False
        
        return self._is_RBT_helper(self.root.right) and self._is_RBT_helper(self.root.left)
    
    def _is_RBT_helper(self, node, parentColor=None):
        if node.color == 1: # if node is red
            return (node.right == None || node.right.color == 0) and (node.left == None || node.left.color == 0)



        
testTree = rbTree()
testTree.root.display()