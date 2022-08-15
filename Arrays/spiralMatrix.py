# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/

class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.visited = set()

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = ['r','d','l','u']
        d = directions[0]
        n = 0
        m = 0
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        total = self.rows * self.cols
        result = []
        while(len(self.visited) < total):
            result.append(matrix[n][m])
            self.visited.add((n,m))
            n,m,d = self.getNext(n,m,d)
            
        return result
                        
            
            
    def oob(self, n, m):
        return (n < 0 or n > self.rows - 1 or m < 0 or m > self.cols - 1)
    
    def isVisited(self, n, m):
        return (n,m) in self.visited
    
    def getNext(self, n, m, d):
        if d == 'r':
            if self.oob(n,m+1) or self.isVisited(n,m+1):
                return n+1, m, 'd'
            else:
                return n, m+1, 'r'
        if d == 'd':
            if self.oob(n+1, m) or self.isVisited(n+1,m):
                return n, m-1, 'l'
            else:
                return n+1,m,'d'
        if d == 'l':
            if self.oob(n,m-1) or self.isVisited(n,m-1):
                return n-1,m,'u'
            else:
                return n,m-1,'l'
        if d == 'u':
            if self.oob(n-1,m) or self.isVisited(n-1,m):
                return n,m+1,'r'
            else:
                return n-1,m,'u'
                
            