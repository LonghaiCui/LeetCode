class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1
        result = [[1 for x in range(m)] for x in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[n-1][m-1]

solution = Solution()
print solution.uniquePaths(8, 4)



