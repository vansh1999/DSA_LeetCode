class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # sqr = []

        # for i in range(len(nums)):
        #     i = nums[i] * nums[i]
        #     i = abs(i)
        #     sqr.append(i)

        
        # sqr.sort()

        # return sqr
    
        # use two pointer for better time complexity 

        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left = left + 1
            else:
                result.append(nums[right] ** 2)
                right = right - 1
        
        result.reverse()

        return result
    
        # O(n) + O(n) -> O(n)

sol = Solution()

print(sol.sortedSquares([-4,-1,0,3,10]))