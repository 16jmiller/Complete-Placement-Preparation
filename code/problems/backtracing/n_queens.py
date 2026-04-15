# The N–queens puzzle is the problem of placing N chess queens on an N × N chessboard so that no two queens threaten each other.
# Thus, the solution requires that no two queens share the same row, column, or diagonal.

# For example, for a standard 8 × 8 chessboard, below is one such configuration:

# Q  –  –  –  –  –  –  – 
# –  –  –  –  Q  –  –  – 
# –  –  –  –  –  –  –  Q 
# –  –  –  –  –  Q  –  – 
# –  –  Q  –  –  –  –  – 
# –  –  –  –  –  –  Q  – 
# –  Q  –  –  –  –  –  – 
# –  –  –  Q  –  –  –  –


def n_queens_try_one(n):
    matrix = [['-' for _ in range(n)] for _ in range(n)]
    rows_map = {i: 0 for i in range(n)}
    cols_map = {i: 0 for i in range(n)}
    left_diags = {i: 0 for i in range(0, 2*n)}
    right_diags = {i: 0 for i in range(-n, n)} 
    for i in range(n):
        for j in range(n):
            if rows_map[i] == 0:
                if cols_map[j] == 0:
                    if left_diags[j+i] == 0:
                        if right_diags[j-i] == 0:
                            rows_map[i] = 1
                            cols_map[j] = 1
                            left_diags[j+i] = 1
                            right_diags[j-i] = 1
                            matrix[i][j] = 'Q'

    return matrix

def n_queens_try_2(n):
    matrix = [['-' for _ in range(n)] for _ in range(n)]
    # visited_matrix = [[0 for _ in range(n)] for _ in range(n)]

    cols_map = {i: 0 for i in range(n)}
    left_diags = {i: 0 for i in range(0, 2*n)}
    right_diags = {i: 0 for i in range(-n, n)}

    # # Initial setup for matrix
    # for i in range(n):
    #     matrix[i][0] = 'Q'

    def is_valid(row, col):
        if cols_map[col] == 0 and left_diags[row+col] == 0 and right_diags[col-row] == 0:
            return True
        
    def backtrace(row, n, matrix, count, isBacktracing=False):
        print(row)
        for i in matrix:
            print(" ".join(f"{val}" for val in i))
        count+=1
        if(count == 15):
            return matrix
        if(row == 0):
            matrix[0][0] = 'Q'
            cols_map[0] = 1
            left_diags[0] = 1
            right_diags[0] = 1
            backtrace(row+1, n, matrix, count)
        visited_col = 0
        if(isBacktracing == True):
            old_col = matrix[row].index('Q')
            cols_map[old_col] = 0
            left_diags[row+old_col] = 0
            right_diags[old_col-row] = 0
            matrix[row] = ['-' for _ in range(n)]
            visited_col = old_col

        found = False;
        for col in range(visited_col+1, n):
            # for a row,col pair, check if valid
            if is_valid(row, col) and visited_col != col:
                # if yes, mark visited and update the final matrix
                matrix[row][col] = 'Q'
                cols_map[col] = 1
                left_diags[row+col] = 1
                right_diags[col-row] = 1
                found = True
                break

            # if no, keep going
        # if not found, go back
        if found == False:
            backtrace(row-1, n, matrix, count, True)

        # if found and row = n, finish
        if(row == n-1):
            return matrix

        # if found and row is not n, keep going
        backtrace(row+1, n, matrix, count)

    return backtrace(0, n, matrix, 0)

def n_queens(n):
    cols_map = {i: 0 for i in range(n)}
    left_diags = {i: 0 for i in range(0, 2*n)}
    right_diags = {i: 0 for i in range(-n, n)}

    board = [['-' for _ in range(n)] for _ in range(n)]
    result = []

    def is_valid(row, col):
        if cols_map[col] == 0 and left_diags[row+col] == 0 and right_diags[col-row] == 0:
            return True
    
    def backtrack(row):
        if(row == n):
            grid_str = "\n".join(" ".join(map(str, row)) for row in board)
            result.append("Solution:\n" + grid_str + "\n\n")
            return
        
        for col in range(n):
            if not is_valid(row,col):
                continue
            board[row][col] = 'Q'
            cols_map[col] = 1
            left_diags[row+col] = 1
            right_diags[col-row] = 1
            backtrack(row+1)
            board[row][col] = '-'
            cols_map[col] = 0
            left_diags[row+col] = 0
            right_diags[col-row] = 0

    backtrack(0)
    return result



if __name__ == '__main__': 
    result = n_queens(9)

    print(result[0])

    # print(*result, sep='\n')

    # for try 1 and try 2
    # for row in result:
    #     print(" ".join(f"{val}" for val in row))

