# LC https://leetcode.com/problems/n-ary-tree-level-order-traversal/
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        answer = []
        queue = [root]
        values_in_level = []
        next_queue = []
        while len(queue) > 0:
            node = queue.pop(0)
            values_in_level.append(node.val)
            
            if node.children:
                for child in node.children:
                    next_queue.append(child)
                    
            if len(queue) == 0:
                answer.append(values_in_level)
                values_in_level = []
                queue = next_queue
                next_queue = []
                
        return answer
            
def test():
    three = Node(3, [Node(5), Node(6)])
    head = Node(1, [three, Node(2), Node(4)])

    #      1
    #  3   2   4
    # 5 6

    # expect [[1],[3,2,4],[5,6]]
    sol = Solution()
    print(sol.levelOrder(head))
test()