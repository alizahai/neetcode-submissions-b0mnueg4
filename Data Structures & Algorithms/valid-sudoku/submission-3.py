class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check 1
        for row in range(9):
            seen = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])
        
        # check 2
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        # check 3
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    # 1. find top-left corner of the square (using square // 3 and square % 3) 
                    # 2. then add i, j to iterate over the boxes inside each square
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
