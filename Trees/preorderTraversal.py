# LC: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorderRecursive(self, root):
        if root is None:
          return []
        
        arr = [root.val]
        if root.children: # not needed on LC
            for child in root.children:
                arr = arr + self.preorderRecursive(child)
        return arr

    def preorderIterative(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        answer = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            answer.append(node.val)
            if node.children: # not needed on LC?
                temp = []
                for child in node.children:
                    temp.append(child)
                queue = temp + queue
        return answer

def test():
    three = Node(3, [Node(5), Node(6)])
    head = Node(1, [three, Node(2), Node(4)])

    #      1
    #  3   2   4
    # 5 6

    # expect [1,3,5,6,2,4]
    sol = Solution()
    print(sol.preorderRecursive(head))
    print(sol.preorderIterative(head))
test()