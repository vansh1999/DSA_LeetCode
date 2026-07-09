class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # use Brute Force - O(n) search

        # rows = len(matrix)
        # cols = len(matrix[0])

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == target:
        #             return True
        
        # return False
    
        # oprtimized - > O(log n*m)
        # apprach - combine all elements as one single arr, since they are sorted

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows*cols - 1

        while l<=r:
            mid = (l+r) // 2

            i = mid // cols
            j = mid % cols

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l=mid+1
            else:
                r=mid-1

        return False


sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 3))