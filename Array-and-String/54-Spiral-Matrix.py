class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # ROWS AND COLS
        m, n = len(matrix) , len(matrix[0])
        ans = []
        i,j = 0 , 0

        UP, RIGHT, DOWN, LEFT = 100, 200, 300 , 400
        direction = RIGHT

        # taking walls outside the matrix
        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1 # left most side . left of 0

        # will consider doing operation with we have all elements , which can be assumed by n X m
        while len(ans) != m*n:

            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j = j + 1
                # j will go outside the wall , so bring it back to matrix
                j = j - 1
                i = i + 1
                # contract the wall 
                RIGHT_WALL = RIGHT_WALL - 1
                # Finally , change direction
                direction = DOWN
            
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i = i + 1
                
                # again bring back i, as it will go outside the matrix
                i = i - 1
                j = j - 1

                DOWN_WALL = DOWN_WALL - 1
                direction = LEFT

            elif direction == LEFT:
                # J will be greater then left wall
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j = j - 1
                
                j = j + 1 
                i = i - 1

                # left wall + 1 >>>
                LEFT_WALL = LEFT_WALL + 1
                direction = UP

            elif direction == UP:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i = i - 1
                i = i + 1
                j = j + 1

                # up wall + 1
                UP_WALL = UP_WALL + 1
                direction = RIGHT

        return ans
        
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

# time = O(n*m)
# space = O(n*m) # result array












        

