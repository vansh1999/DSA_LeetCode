nums = [0,1,2,2,3,0,4,2]

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        
        occ = 0

        for i in nums:
            if i == val:
                occ = occ + 1
        
        k = len(nums) - occ


        return k
    

sol = Solution()
print(sol.removeElement(nums, 2))
