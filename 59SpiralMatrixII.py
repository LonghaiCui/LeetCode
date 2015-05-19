# class Solution:
#     #@param {integer[][]} matrix
#     #@return {integer[]}
#     def spiralOrder(self, matrix):
#         if not matrix:
#             return []
#         left = 0
#         right = len(matrix[0]) - 1
#         up = 0
#         bottom = len(matrix) - 1
#         ret = []
#         while left <= right and up <= bottom:
#             if left == right:
#                 for i in range(up,bottom+1):
#                     ret.append(matrix[i][left])
#                 break
#             if up == bottom:
#                 for i in range(left,right+1):
#                     ret.append(matrix[bottom][i])
#                 break
#             for i in range(left, right+1):
#                 ret.append(matrix[up][i])
#                 #print 'a', matrix[up][i]
#             for i in range(up+1, bottom+1):
#                 ret.append(matrix[i][right])
#                 #print 'b', matrix[i][right]
#             for i in reversed(range(left, right)):
#                 ret.append(matrix[bottom][i])
#                 #print 'c', matrix[bottom][i]
#             for i in reversed(range(up+1,bottom)):
#                 ret.append(matrix[i][left])
#                 #print 'd', matrix[i][left]
#             up += 1
#             right -= 1
#             bottom -= 1
#             left += 1
#         return ret

# class Solution:
#     # @param {integer} n
#     # @return {integer[][]}
#     def generateMatrix(self, n):
#         if n == 0:
#             return []
#         matrix = [[0 for x in range(n)] for x in range(n)]
#         left = up = 0
#         right = bottom = n - 1
#         cur = 1
#         while left < right and up < bottom:
#             for i in xrange(left, right+1):
#                 matrix[up][i] = cur
#                 cur += 1
#             for i in xrange(up+1, bottom+1):
#                 matrix[i][right] = cur
#                 cur += 1
#             for i in reversed(xrange(left, right)):
#                 matrix[bottom][i] = cur
#                 cur += 1
#             for i in reversed(xrange(up+1, bottom)):
#                 matrix[i][left] = cur
#                 cur += 1
#             up += 1; right -= 1; bottom -= 1; left += 1
#
#         if n % 2 == 0:
#             matrix[up][up] = cur
#         return matrix
#
# solution = Solution()
# print solution.generateMatrix(5)

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [[0 for x in range(n)] for x in range(n)]
        left = 0
        right = n - 1
        cur = 1
        while left < right:
            for i in xrange(left, right+1):
                matrix[left][i] = cur
                cur += 1
            for i in xrange(left+1, right+1):
                matrix[i][right] = cur
                cur += 1
            for i in reversed(xrange(left, right)):
                matrix[right][i] = cur
                cur += 1
            for i in reversed(xrange(left+1, right)):
                matrix[i][left] = cur
                cur += 1
            right -= 1;
            left += 1
        if n % 2 == 1:
            matrix[left][left] = cur
        return matrix

solution = Solution()
print solution.generateMatrix(3)

