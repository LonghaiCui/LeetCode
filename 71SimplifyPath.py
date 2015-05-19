class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        pass

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 4:
            return n
        x1 = 2
        x2 = 3
        for i in range(n-3):
            x3 = x1 + x2
            x1 = x2
            x2 = x3
        return x3

solution = Solution()
print solution.climbStairs(3)

