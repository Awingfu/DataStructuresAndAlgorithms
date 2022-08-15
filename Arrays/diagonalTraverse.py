# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/

class Solution:
    
    def __init__(self):
        self.rows = 0
        self.cols = 0
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0,0 -> 0,1 -> 1,0 -> 2,0 -> 1,1 -> 0,2
        # start at 0,0 moving up -> if moving up, check row -1, col+1. if oob, moving down, start row, col+1
        # if moving down, check row+1,col-1, if oob, moving up, start row+1,col
        
        n = 0
        m = 0
        self.rows = len(mat) -1
        self.cols = len(mat[0]) -1
        movingUp = True
        
        result = []
        # could be while true
        while n < len(mat) and m < len(mat[0]):
            result.append(mat[n][m])
            # print('appending ' + str(mat[n][m]))
            # print('currently at ' + str(n) + ', ' + str(m))
            if n == len(mat) and m == len(mat[0]):
                break
            if movingUp:
                if self.oob(n-1,m+1):
                    n,m = self.findNext(n,m,movingUp)
                    movingUp = False
                else:
                    n -= 1
                    m += 1
            else:
                if self.oob(n+1, m-1):
                    n,m = self.findNext(n,m,movingUp)
                    movingUp = True
                else:
                    n += 1
                    m -= 1
                    
            # print('movingUp ' + str(movingUp))
            # print('checking ' + str(n) + ', ' + str(m))
        return result
    
    def oob(self, r, c):
        oob = (r < 0 or r > self.rows or c < 0 or c > self.cols)
        # if oob:
        #     print(str(r) + ',' + str(c) + ' is oob')
        # else:
        #     print(str(r) + ',' + str(c) + ' is in bounds')
        return oob
    
    def findNext(self,n,m,movingUp):
        if movingUp:
            # check right, otherwise down
            if self.oob(n, m+1):
                return n+1, m
            else:
                return n, m+1
        else:
            # check bottom, otherwise right
            if self.oob(n+1, m):
                return n,m+1
            else:
                return n+1,m