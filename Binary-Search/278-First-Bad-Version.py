# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:


        # Brute Force - O(n)
        # for x in range(1, n+1):
        #     if isBadVersion(x):
        #         return x
            
        # Binary search - O(log n)
        
        l = 1 
        r = n

        while l<r:

            mid  = (l+r) // 2

            if isBadVersion(mid):
                r = mid 
            else:
                l=mid+1

        return l

# note
# If no, you're doing exact-match search → l <= r, exclude mid both ways.
# If yes, you're doing boundary search → l < r, keep mid on one side.