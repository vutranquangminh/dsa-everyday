class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def soduku(valid):
            dic = {}
            check = []
            for i in range(9):
                if valid[i] != '.':
                    if int(valid[i]) not in check:
                        check.append(int(valid[i]))
                    else:
                        return 1
            
            return 0        

        anwser = 0
        arr = []
        for i in range(9):       
            row = []
            for j in range(9):
                arr.append(board[i][j])                
                if board[i][j] != '.':
                    if int(board[i][j]) not in row:
                        row.append(int(board[i][j]))
                    else:
                        return False
        
        for i in range(9):       
            col = []
            for j in range(9):
                if board[j][i] != '.': 
                    if int(board[j][i]) not in col:
                        col.append(int(board[j][i]))
                    else:
                        return False

        start = 0
        for i in range(9):
            test = []
            for j in range(start,start+3):
                test.append(arr[j])
                test.append(arr[j+9])
                test.append(arr[j+18])
            anwser += soduku(test)
            if start == 6:
                 start = 24
            elif start == 33:
                start = 51
            start += 3
    
        if anwser == 0:
            return True
        return False