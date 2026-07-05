from typing import List


nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        new_arr = []

        for i in nums:
            if i not in new_arr:
                new_arr.append(i)
            else:
                continue

        for i in range(len(new_arr)):
            nums[i] = new_arr[i]

        k = len(new_arr)
        

        # print(k , ", nums =" , new_arr , sep="")

        return k

sol = Solution()
sol.removeDuplicates(nums)

# current Problem 
# 1. Creates a new array (new_arr) instead of modifying nums. -> done
# 2. Doesn’t return k -> done 

