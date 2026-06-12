from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        
        def backtrack(i, j, index):
            if index == w:
                return True
            
            if (i < 0 or i >= m or j < 0 or j >= n or 
                board[i][j] != word[index]):
                return False
            
            temp = board[i][j]
            board[i][j] = "*"
            
            for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if backtrack(i + i_off, j + j_off, index + 1):
                    return True
            
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False