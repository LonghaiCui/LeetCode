class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

solution = Solution()
print solution.minPathSum([[0,0],[1,0],[0,0],[1,0],[0,0],[0,1],[1,0],[0,0],[0,0],[0,1],[0,1],[0,0],[1,0],[0,0]]
)

