
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # not using transpose and reflection
        # using Left -> Top
        # Bottom -> left
        # right -> bottom
        # top -> right
        # repeat for all n layer

        n = len(matrix)

        # which ring you’re working on
        for layer in range(n//2):
            left = layer
            right = n - 1 - layer

            for col in range(left,right):

                # where you are inside that ring
                offset = col - left

                top = matrix[left][col]

                # left -> top
                matrix[left][col] = matrix[right - offset][left]

                # bottom -> left
                matrix[right - offset][left] = matrix[right][right - offset]

                # right -> botom
                matrix [right][right - offset] = matrix[left+ offset][right]

                # top -> right
                matrix[left + offset][right] = top


# Time -> O(n^2)
# Space -> O(1)   

