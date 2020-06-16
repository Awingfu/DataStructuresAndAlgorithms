# implemented with help from https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

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

class AVL_Tree():

    def insert(self, root, val): 
        if root == None:
            root = Node(val)
            return root
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))

        balance = self.getBalance(root)

        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and val < root.right.val: 
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root


    def getHeight(self, node):
        if node == None:
            return 0
        return node.height

    def getBalance(self, node):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, node):
        node.display()
        print('left rotation on ' + str(node.val))
        y = node.right
        T2 = y.left

        # rotate
        y.left = node
        node.right = T2

        # update heights
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        y.display()
        return y

    def rightRotate(self, node):
        node.display()
        print('right rotation on ' + str(node.val))
        y = node.left
        T3 = y.right

        # rotate
        y.right = node
        node.left = T3

        # update heights
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        y.display()
        return y

testTree = AVL_Tree()
print("inserting 10")
root = testTree.insert(None, 10)
print("result:")
root.display()
print("inserting 20")
root = testTree.insert(root, 20) 
print("result:")
root.display()
print("inserting 30")
root = testTree.insert(root, 30) 
print("result:")
root.display()
print("inserting 40")
root = testTree.insert(root, 40) 
print("result:")
root.display()
print("inserting 50")
root = testTree.insert(root, 50) 
print("result:")
root.display()
print("inserting 25")
root = testTree.insert(root, 25) 
print("result:")
root.display()