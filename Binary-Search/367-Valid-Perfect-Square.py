class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Brute force -> O(sqrt n)

        # i = 1
        
        # while i**2 <= num:

        #     if i**2 == num:
        #         return True
            
        #     print(i)

        #     i=i+1
        
        # return False

        # Binary Search - O(log n)

        l = 1
        r = num

        while l<=r:

            mid = (l+r) // 2

            if mid**2 == num:
                return True
            elif mid**2 < num:
                l=mid+1
            else:
                r=mid-1
        
        return False


sol = Solution()
print(sol.isPerfectSquare(25))