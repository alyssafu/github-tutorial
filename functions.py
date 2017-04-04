def islandPerimeter(grid):
    """
    The solution to today's leetcode challenge.
    :type grid: List[List[int]]
    :rtype: int
    """
    
    leni = len(grid)
    lenj = len(grid[0])

    def countCell(i,j):
        if not grid[i][j]:
            return 0
        borders = 4
        if i>0 and grid[i-1][j]: borders -= 1
        if i<(leni-1) and grid[i+1][j]: borders -= 1
        if j<(lenj-1) and grid[i][j+1]: borders -= 1
        if j>0 and grid[i][j-1]: borders -= 1
        return borders
    
    return sum([countCell(i,j) for i in range(leni) for j in range(lenj)])
