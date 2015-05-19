# class Solution:
#     # @param {integer} n
#     # @return {integer}
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         x1 = 1
#         x2 = 2
#         for i in range(3, n+1):
#             x3 = x1 + x2
#             x1 = x2
#             x2 = x3
#         return x3


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 3:
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

