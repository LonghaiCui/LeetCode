# class Solution:
#     # @param {integer[][]} matrix
#     # @return {void} Do not return anything, modify matrix in-place instead.
#     def rotate(self, matrix):
#         cur_x = 0
#         for cur_y in range(len(matrix)-1):
#             next = matrix[0][cur_y]
#             for j in range(4):
#                 print next
#                 new_x = cur_y
#                 new_y = len(matrix)-1-cur_x
#
#                 temp = matrix[new_x][new_y]
#                 matrix[new_x][new_y] = next
#                 next = temp
#
#                 cur_x = new_x
#                 cur_y = new_y
#         print matrix

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        for i in range(len(matrix)/2):
            for cur_y in range(i,len(matrix)-i-1):
                cur_x = i
                # temp = matrix[cur_x][cur_y]
                # matrix[cur_x][cur_y] = matrix[len(matrix)-1-cur_y][cur_x]
                # matrix[len(matrix)-1-cur_y][cur_x] = matrix[len(matrix)-1-cur_x][len(matrix)-1-cur_y]
                # matrix[len(matrix)-1-cur_x][len(matrix)-1-cur_y] = matrix[cur_y][len(matrix)-1-cur_x]
                # matrix[cur_y][len(matrix)-1-cur_x] = temp

                matrix[cur_x][cur_y], matrix[len(matrix)-1-cur_y][cur_x], \
                    matrix[len(matrix)-1-cur_x][len(matrix)-1-cur_y], matrix[cur_y][len(matrix)-1-cur_x] = \
                    matrix[len(matrix)-1-cur_y][cur_x], matrix[len(matrix)-1-cur_x][len(matrix)-1-cur_y],\
                    matrix[cur_y][len(matrix)-1-cur_x],matrix[cur_x][cur_y]

        print matrix

#print solution.rotate(None)
#solution.rotate([[1]])
#solution.rotate([[1,2],[3,4]])
#solution.rotate([[1,2,3],[4,5,6],[7,8,9]])


# Output:	[[13,9,5,1],[14,6,7,2],[15,10,11,3],[16,12,8,4]]
# Expected:	[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print matrix
solution = Solution()
solution.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if matrix is None:
            return

        m = len(matrix)

        for i in range(m):
            for j in range(i,m-i-1):
                row = j
                col = m-1-i
                while not (row == i and col == j):
                    mid = matrix[row][col]
                    matrix[row][col] = matrix[i][j]
                    matrix[i][j] = mid
                    row1 = row
                    col1 = col
                    row = col1
                    col = m-1-row1