# LC: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorderRecursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        arr = []
        if root.children:        
            for child in root.children:
                arr = arr + self.postorderRecursive(child)
        return arr + [root.val]

    def postorderIterative(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        answer = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop()
            answer.insert(0,node.val)
            if node.children:
                for child in node.children:
                    queue.append(child)
        return answer

def test():
    three = Node(3, [Node(5), Node(6)])
    head = Node(1, [three, Node(2), Node(4)])

    #      1
    #  3   2   4
    # 5 6

    # expect [5,6,3,2,4,1]
    sol = Solution()
    print(sol.postorderRecursive(head))
    print(sol.postorderIterative(head))
test()