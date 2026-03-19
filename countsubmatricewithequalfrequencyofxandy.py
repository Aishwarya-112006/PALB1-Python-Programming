'''Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]'''

lass Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
      
        val = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        
        count = 0
        
       
        for i in range(m):
            for j in range(n):
                if i > 0:
                    val[i][j] += val[i-1][j]
                if j > 0:
                    val[i][j] += val[i][j-1]
                if i > 0 and j > 0:
                    val[i][j] -= val[i-1][j-1]
                
                
                if val[i][j] == 0:
                   
                    hasX = False
                    for x in range(i+1):
                        for y in range(j+1):
                            if grid[x][y] == 'X':
                                hasX = True
                                break
                        if hasX:
                            break
                    
                    if hasX:
                        count += 1
        
        return count
