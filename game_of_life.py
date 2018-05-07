class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        coordinate_1 = set()
        coordinate_0 = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                if j-1>=0 and board[i][j-1] == 1:
                    count += 1
                if j+1<len(board[i]) and board[i][j+1] == 1:
                    count += 1
                if i-1>=0 and board[i-1][j] == 1:
                    count += 1
                if i+1< len(board) and board[i+1][j] == 1:
                    count += 1
                if j-1>=0 and i-1>=0 and board[i-1][j-1] == 1:
                    count += 1
                if j-1>=0 and i+1 <len(board) and board[i+1][j-1] == 1:
                    count += 1
                if j+1<len(board[i]) and i-1>=0 and board[i-1][j+1] == 1:
                    count += 1
                if j+1<len(board[i]) and i+1< len(board) and board[i+1][j+1]== 1:
                    count += 1

                if count<2 or count>3:
                    coordinate_0.add((i,j))

                if count == 3:
                    if board[i][j] == 0:
                        coordinate_1.add((i,j))

        for element in coordinate_1:
            board[element[0]][element[1]] = 1
        for element in coordinate_0:
