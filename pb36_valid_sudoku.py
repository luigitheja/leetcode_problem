class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #needs reforms forsuhre

        def check_row_violation(board1):

            for row in board1:
                current_row_vals = [int(row_val) for row_val in row if row_val != "."]
                if len(list(set(current_row_vals))) < len(current_row_vals) :
                    return False
            
            return True
        
        def transposed(board1):
            return [[board1[j][i] for j in range(len(board1))] for i in range(len(board1[0]))]

        
        if not (check_row_violation(board) and check_row_violation(transposed(board))):
            return False
        
        subgrids = {}

        for col in range(0, len(board)):

            for row in range(0, len(board[0])):
                
                subgrid_ind = str(col//3) + str(row//3) 
                element = board[col][row]

                if element != ".":
                    if subgrid_ind in subgrids.keys():
                        subgrids[subgrid_ind].append(element)                
                    else:
                        subgrids[subgrid_ind] = [element]
        
        subgrid_matrix = [subgrid for subgrid in subgrids.values()]

        print(subgrids)

        return check_row_violation(subgrid_matrix)
        # for subgrid in subgrids.values():
        #     print(subgrid)
        #     if not check_row_violation(subgrid):
        #         return False
        
        # return True
                





                