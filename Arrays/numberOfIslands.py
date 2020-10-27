# https://leetcode.com/problems/number-of-islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # no grid -> return 0
        # double for loop, if detect 1, increment islandcounter
        # helper function on grid and location, mark all adjacent 1's as 0's
        # until exhaustion - edges are 0 or edge
        # return island counter
        if grid is None:
            return 0
        island_count = 0
        for row_ind in range(len(grid)):
            for col_ind in range(len(grid[0])): #O(h*w)
                if grid[row_ind][col_ind] == "1":
                    island_count += 1
                    self.markIsland(row_ind, col_ind, grid)
        return island_count
    
    def markIsland(self, row, col, grid): # O(h*w)
        grid[row][col] = "0"
        # look up
        if row != 0 and grid[row-1][col] == "1":
            self.markIsland(row-1, col, grid)
        # look left
        if col != 0 and grid[row][col-1] == "1":
            self.markIsland(row, col-1, grid)
        # look down
        if row != len(grid)-1 and grid[row+1][col] == "1":
            self.markIsland(row+1, col, grid)
        # look right
        if col != len(grid[0])-1 and grid[row][col+1] == "1":
            self.markIsland(row, col+1, grid)

        # 
        # queue = [(row,col)]
        # while len(queue) > 0:
        #     print(queue)
        #     row, col = queue.pop(0) #not a true queue, O(n) operation
        #     # print(row,col)
        #     grid[row][col] = "0"
        #     # look up
        #     if row != 0 and grid[row-1][col] == "1":
        #         queue.append((row-1,col))
        #     # look left
        #     if col != 0 and grid[row][col-1] == "1":
        #         queue.append((row,col-1))
        #     # look down
        #     if row != len(grid)-1 and grid[row+1][col] == "1":
        #         queue.append((row+1,col))
        #     # look right
        #     if col != len(grid[0])-1 and grid[row][col+1] == "1":
        #         queue.append((row,col+1))
        # return grid

test = Solution()
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid3 = [
  ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
  ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
  ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
  ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
  ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]
# print(test.numIslands(grid1) == 1)
# print(test.numIslands(grid2) == 3)
print(test.numIslands(grid3))