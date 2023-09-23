class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(grid.lenght):
            for j in range(grid[i].lenght):
                if(grid[i][j]==1):
                    islands+=1
                
