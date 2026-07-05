class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []
        i = 0

        while i < len(nums):

            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i = i + 1
            
            if start != nums[i]:
                res.append(str(start) + ' -> ' + str(nums[i]))
            else:
                res.append(str(nums[i]))
            
            i = i + 1
        
        return res


sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))

# Time complexity -> O(n) even tho we gave 2 while loops, we are iterating nums and moving forward once, i only moves forward and never resets.
# Space complexity -> O(n) -> for every nums we are storing extra res