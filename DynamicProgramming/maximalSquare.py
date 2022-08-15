# https://leetcode.com/problems/maximal-square/submissions/
# 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # recursive
        # dfs from top left (0,0)
        # recursive, if value of self is 1, can make square 1
        # then + min (check right, down, down-right) to determine if you can make bigger square
        # cache to keep max length of a valid square. then return max(cache) ** 2 to get area of largest square
        
        # ROW, COL = len(matrix), len(matrix[0])
        # cache = {}
        
        # # helper to return the longest square length
        # def helper(r, c):
        #     # out of bounds
        #     if r >= ROW or c >= COL:
        #         return 0
            
        #     if (r,c) not in cache:
        #         down = helper(r+1, c)
        #         right = helper(r, c+1)
        #         down_right = helper(r+1,c+1)
                
        #         cache[(r,c)] = 0
        #         if matrix[r][c] == '1':
        #             cache[(r,c)] = 1 + min(down,right,down_right)
                    
        #     return cache[(r,c)]
        
        # helper(0,0)
        # return max(cache.values()) ** 2
        
        # bottom up
        result = [ [0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(0,len(matrix)):
            for c in range(0,len(matrix[0])):
                val = int(matrix[r][c])
                if val != 1:
                    continue
                if r == 0 or c == 0:
                    result[r][c] = val
                    continue
                up = result[r-1][c]
                left = result[r][c-1]
                up_left = result[r-1][c-1]
                result[r][c] = 1 + min(up,left,up_left)
                
        print(result)
        return max(list(map(max, result))) ** 2
                    
        # space optimal bottom up
                # optimal bottom up
        ROW, COL = len(matrix), len(matrix[0])
        cache = [ [0] * COL for _ in range(ROW)]

        for i in range(COL):
            cache[0][i] = int(matrix[0][i])
            
        max_length = max(cache[0])
    
        for r in range(1,ROW):
            for c in range(0,COL):
                val = int(matrix[r][c])
                if val != 1:
                    continue
                if c == 0:
                    cache[1][c] = val
                    max_length = max(max_length, cache[1][c])
                    continue
                up = cache[0][c]
                left = cache[1][c-1]
                up_left = cache[0][c-1]
                cache[1][c] = 1 + min(up,left,up_left)
                max_length = max(max_length, cache[1][c])
            # shift values up
            for i in range(COL):
                cache[0][i] = cache[1][i]
                cache[1][i] = 0
                            
        print(cache)
        print(max_length)
        return max_length ** 2