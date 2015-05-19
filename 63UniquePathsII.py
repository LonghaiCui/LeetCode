class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            for i in range(n):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1
        if n == 1:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
                break

        for j in range(i+1, n):
            obstacleGrid[0][j] = 0

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                break

        for j in range(i+1, m):
            obstacleGrid[j][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        for i in obstacleGrid:
            print i
        return obstacleGrid[m-1][n-1]

solution = Solution()
print solution.uniquePathsWithObstacles([[0,0],[1,0],[0,0],[1,0],[0,0],[0,1],[1,0],[0,0],[0,0],[0,1],[0,1],[0,0],[1,0],[0,0]]
)
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # if m == 1:
        #     for i in range(n):
        #         if obstacleGrid[0][i] == 1:
        #             return 0
        #     return 1
        # if n == 1:
        #     for i in range(m):
        #         if obstacleGrid[i][0] == 1:
        #             return 0
        #    return 1
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
                break

        for j in range(i+1, n):
            obstacleGrid[0][j] = 0

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                break

        for j in range(i+1, m):
            obstacleGrid[j][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #Adjust the values in the first row
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
                break
        #Set the rest in the first row to 0
        for j in range(i+1, n):
            obstacleGrid[0][j] = 0
        #Adjust the values in the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                break
        #Set the rest in the first column to 0
        for j in range(i+1, m):
            obstacleGrid[j][0] = 0
        #Same with uniquePaths except that set the value to 0 if for the obstables
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]


class Solution:
# @param obstacleGrid, a list of lists of integers
# @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
        ResGrid[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]

        return ResGrid[m][n]