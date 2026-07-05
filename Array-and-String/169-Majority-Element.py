class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # brute force -> time -> O(n^2)
        # use Hash map -> time -> O(n)

        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count = count+1
                if count > n//2:
                    return nums[i]

        

sol = Solution()
print(sol.majorityElement([3,2,3]))


        # count = {}
        # maj = len(nums) // 2

        # for i in nums:
        #     if i in count:
        #         count[i] = count[i] + 1
        #     else:
        #         count[i] = 1
            
        #     if count[i] > maj:
        #         return i
