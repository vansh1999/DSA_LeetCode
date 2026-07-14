class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # M3 -> use 2 pointer -> time -> O(n) and space -> O(1)

        # use L to keep track of 0, and where non 0 should go
        # use R as scannig pointer


        l = 0

        for r in range(len(nums)):

            if nums[r] != 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                l = l + 1
            

        # M1 Own - Brute Force - O(2n)

        # arr = []


        # for j in nums:
        #     if j != 0:
        #         arr.append(j)

        # for i in nums:
        #     if i == 0:
        #         arr.append(0)

        
        # nums = arr

        # return nums
    

        # M2 Do not return -> O(n^2)

        # For -> n
        # remove -> n

        # for i in range(len(nums)):

        #     if nums[i] == 0:
        #         nums.remove(nums[i])
        #         nums.append(0)
        #     else:
        #         continue

        
        # return nums



sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))