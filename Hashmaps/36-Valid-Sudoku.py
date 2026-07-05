class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # validate Rows

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]

                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # validate Cols

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]

                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
    


        # validate 3X3 boxes

        starts = [(0,0) , (0,3) , (0,6) ,
                  (3,0) , (3,3) , (3,6) ,
                  (6,0) , (6,3) , (6,6)
                  ] 
        
        for i, j in starts:
            s = set()
            for row in range(i , i+3):
                for col in range(j , j+3):
                    item = board[row][col]

                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True


        # Time -> constant for 9X9 board -> O(1)
        # for N*N board -> O(n^2)


sol = Solution()

print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))