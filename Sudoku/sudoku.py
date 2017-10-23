def isValidSudoku(self, board):
        for i in range(9):
            
            row = [False for x in xrange(9)]
            column = [False for x in xrange(9)]
            square = [False for x in xrange(9)]
            for j in range (9):
                #parse int subtract one accounting for index
                if board[i][j] != ".":
                    row_value = int(board[i][j]) - 1
                    if row[row_value] == False:
                        row[row_value] = True
                    else:
                        return False
                if board[j][i] != ".":
                    col_value = int(board[j][i]) - 1
                    if column[col_value] == False:
                        column[col_value] = True
                    else:
                        return False
                
                colindex = 3*(i/3) + (j/3)
                rowindex = 3*(i%3)+ (j%3)
                if board[colindex][rowindex] != ".":
                    
                    square_value = int(board[colindex][rowindex]) - 1
                    
                    if square[square_value] == False:
                        square[square_value] = True
                    else:
                        return False
        return True