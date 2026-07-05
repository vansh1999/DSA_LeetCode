class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we can have 2 for loop i and j and have done in O(n^2)

        # lets do in O(n) 
        # hashmap
        # concept and method is really imp for this one
        # keep h with latest i
        # now go through nums and see i can h can validate target-nums[i]

        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i
        
        for j in range(len(nums)):
            y = target - nums[j]

            if y in h and h[y] != j:
                return [j , h[y]]

        # time -> O(n)
            

sol = Solution()
print(sol.twoSum([2,7,11,15,2] , 9))