class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def check_safe_to_place(element, row, col):
            for i in range(9):
                if board[row][i] ==element or board[i][col] == element or board[3*(row//3)+(i//3)][3*(col//3)+(i%3)] == element:
                    return False
            return True



        
        
        def solve():

            solved = True

            for row in board:
                if '.' in row:
                    solved = False
                    break
            
            if solved:
                return True

            for row in range(len(board)):

                for col in range(len(board[0])):

                    if board[row][col] == '.':

                        for stri in map(str, range(1, 10)):
                            
                            if check_safe_to_place(stri, row, col):
                                board[row][col] = stri
                                if solve():
                                    return True
                                board[row][col] = '.'

                        return False
            
            return True
        
        solve()
        return board



