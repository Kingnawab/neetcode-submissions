class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            duplicate = set()
            for i in range(9):
                if board[r][i] == '.':
                    continue
                if board[r][i] in duplicate:
                    return False
                duplicate.add(board[r][i])    
        for col in range(9):
            duplicate = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in duplicate:
                    return False
                duplicate.add(board[i][col])
        for box_row in range(3):
            for box_col in range(3):
                duplicate = set()
                for i in range(3):
                    for j in range(3):
                        r = box_row * 3 + i
                        c = box_col * 3 + j
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in duplicate:
                            return False
                        duplicate.add(board[r][c])
        return True
