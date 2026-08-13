class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isvalid(board[i]):
                return False
        for i in range(9):
            if not self.isvalid([board[row][i] for row in range(9)]):
                return False

        for i in range(9):
            m = i % 3
            n = i // 3
            square = [
                element 
                for row in board[m*3 : (m+1)*3] 
                for element in row[n*3 : (n+1)*3]
            ]
            if not self.isvalid(square):
                return False
        
        return True

    def isvalid(self, elements: List[str]) -> bool:
        ele = {}
        for e in elements:
            if e == '.':
                continue
            elif e in ele:
                return False
            else:
                ele[e] = True
        return True