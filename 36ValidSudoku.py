class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # for row in board:
        #     # cur_row = ''
        #     # for ele in row:
        #     #     if '.' == ele:
        #     #         cur_row += ' '
        #     #     else:
        #     #         cur_row += str(ele)
        #     print row
        #Check for row 9 times
        for row in board:
            visited = {}
            for ele in row:
                if ele != '.':
                    if visited.has_key(ele):
                        return False
                    else:
                        visited[ele] = 1
        #Check for column 9 times
        for i in range(9):
            visited = {}
            for j in range(9):
                ele = board[j][i]
                if ele != '.':
                    if visited.has_key(ele):
                        return False
                    else:
                        visited[ele] = 1

        #Check for column 9 times
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                #print i,j
                visited = {}
                for x in range(3):
                    for y in range(3):
                        #print x, y
                        ele = board[i+x][j+y]
                        if ele != '.':
                            if visited.has_key(ele):
                                return False
                            else:
                                visited[ele] = 1
                        #print i+x,j+y
                j += 3
            i += 3
        return True


# print solution.isValidSudoku([
#     [5,3,'.','.',7,'.','.','.','.'],
#     [6,'.','.',1,9,5,'.','.','.'],
#     ['.',9,8,'.','.','.','.',6,'.'],
#     [8,'.','.','.',6,'.','.','.',3],
#     [4,'.','.',8,'.',3,'.','.',1],
#     [7,'.','.','.',2,'.','.','.',6],
#     ['.',6,'.','.','.','.',2,8,'.'],
#     ['.','.','.',4,1,9,'.','.',5],
#     ['.','.','.','.',8,'.','.',7,9]
#     ])

solution = Solution()
print solution.isValidSudoku(["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."])



class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row
        for row in board:
            if self.isDuplicate(row):
                return False

        # check column
        for i in xrange(0,9):
            if self.isDuplicate([board[j][i] for j in range(0,9)]):
                return False

        # check 3x3
        index = [[0,1,2],[3,4,5],[6,7,8]]
        for x3 in index:
            for y3 in index:
                if self.isDuplicate([board[i][j] for i in x3 for j in y3]):
                    return False

        return True


    def isDuplicate(self, *args):
        l = filter(lambda a: a != '.', args[0])
        return (len(set(l)) - len(l)) != 0
