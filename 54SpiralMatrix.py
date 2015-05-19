class Solution:
    #@param {integer[][]} matrix
    #@return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        bottom = len(matrix) - 1
        ret = []
        while left <= right and up <= bottom:
            if left == right:
                for i in range(up,bottom+1):
                    ret.append(matrix[i][left])
                break
            if up == bottom:
                for i in range(left,right+1):
                    ret.append(matrix[bottom][i])
                break
            for i in range(left, right+1):
                ret.append(matrix[up][i])
                #print 'a', matrix[up][i]
            for i in range(up+1, bottom+1):
                ret.append(matrix[i][right])
                #print 'b', matrix[i][right]
            for i in reversed(range(left, right)):
                ret.append(matrix[bottom][i])
                #print 'c', matrix[bottom][i]
            for i in reversed(range(up+1,bottom)):
                ret.append(matrix[i][left])
                #print 'd', matrix[i][left]
            up += 1
            right -= 1
            bottom -= 1
            left += 1
        return ret
solution = Solution()
print solution.spiralOrder([
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
])
# print solution.spiralOrder([
# [ 1, 2, 3, 4 ],
# [ 5, 6, 7, 8 ],
# [ 9,10,11,12 ]
# ])
print solution.spiralOrder([[3],[2]])
print solution.spiralOrder([])
print solution.spiralOrder([[2,3]])
# [1,2,3,6,9,8,7,4,5]


