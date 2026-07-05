class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        l = 0
        r = n -1 

        max_area = 0

        while l < r:

            w = r - l
            h = min(height[l] , height[r])

            area = w * h

            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l = l + 1
            
            else:
                r = r - 1

        return max_area
    
        # Time -> O(n) Space -> O(1)

    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))