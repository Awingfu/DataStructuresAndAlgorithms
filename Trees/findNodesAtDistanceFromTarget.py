# given an example 3 level tree
#    1
#  2  3 
# 4 5 6 7
# target is 5, distance is 3
# dfs, youd 1,2,5 (store this on a stack & hash map) 
# distance of 3 from 5, distance of 2 form 2, distance of 1 from 1, and also not in stack

# first find the target
# depth first search, but also path from root (to keep track of parents)
# using a stack to store children from parent, then when you pop a node, you push that nodes children
# push 1, pop 1, push 2 & 3, pop 3, push 6 & 7,pop 7,  pop 6,  pop 2 , push 4 & 5, pop 4, pop 5 (target)

# after findTarget, from the root i know the targetDistance is 2 ( i would need to find nodes 3-2) 1 waay from root

# root node, left side returns 2, right side return -1 
# class Node: 
#     val: number
#     left; Node
#     right: Node
#     parent: Null

# mainfxn: 
# Annotate nodes -> dfs, annotates parents, void return
# findTarget (root, target) # returns target node instance
#      findTarget root.left , target
#      findTarget root.right, target
# findNodesAtDistance # bfs from target node to x distance, using set to not queue visited nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BT:
    def __init__(self):
        #    1
        #  2   3 
        # 4 5  6 7
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right = Node(3)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
    
    # Visit all nodes by DFS and annotate parents - O(N)
    def annotateNodeParents(self, root, parent=None):
        if parent != None:
            root.parent = parent
        if root.left != None:
            self.annotateNodeParents(root.left, root)
        if root.right != None:
            self.annotateNodeParents(root.right, root)

    # Return node with targetValue by DFS - O(N)
    def findTarget(self, root, targetValue): 
        if root == None:
            return None
        if root.value == targetValue: 
            return root
        return self.findTarget(root.left, targetValue) or self.findTarget(root.right, targetValue)

    # Return array of nodes (values) that are at distance away from root
    # breadth first search with a 2 directional graph
    # O(n + edges)? 
    def findNodesAtDistance(self, root, distance): 
        if distance == 0:
            return [root.value]

        visitedNodes = set()
        result = []
        visitQueue = [root]
        layerQueue = []

        # While there are things to visit and distance is greater than 0
        while (len(visitQueue) > 0 or len(layerQueue) > 0) and distance > 0:
            if len(visitQueue) == 0:
                visitQueue = layerQueue
                layerQueue = []
                distance -= 1

            tempNode = visitQueue.pop(0)
            # make a list of neighbors
            adjacentNodes = [tempNode.left, tempNode.right, tempNode.parent]

            # if distance == 1, neighbors that havent been seen are results
            if distance == 1:
                for node in adjacentNodes:
                    if node != None and node not in visitedNodes:
                        # Change to result.append(node) to append node object rather than value
                        result.append(node.value)

            # add current node to visited
            if tempNode not in visitedNodes:
                visitedNodes.add(tempNode)
            # for all adjacent nodes, enqueue unvisited nodes
            for node in adjacentNodes:
                if node == None:
                    continue
                if node not in visitedNodes:
                    layerQueue.append(node)

        return result
        
    def findNodesAtDistanceFromTarget(self, root, targetValue, distance):
        # Convert BT implementation to doulbly linked nodes
        self.annotateNodeParents(root) # O(N) where N is number of nodes

        targetNode = self.findTarget(root, targetValue) # O(N) where N is number of nodes
        
        if targetNode == None: 
            print('Unable to find target node')
            return []
        
        return self.findNodesAtDistance(targetNode, distance) # O(N + edges) where N is number of nodes

testBT = BT()
print(testBT.findNodesAtDistanceFromTarget(testBT.root, 5, 2))
print(testBT.findNodesAtDistanceFromTarget(testBT.root, 5, 0))
print(testBT.findNodesAtDistanceFromTarget(testBT.root, 5, 3))