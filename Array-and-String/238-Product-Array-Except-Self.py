class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create two arr L and R , multiple all from left to right and all from right to left in L and R, then need to mul L*R each
        l_mult = 1
        r_mult = 1

        n = len(nums)

        l_arr = [0] * n # [0,0,0,0]
        r_arr = [0] * n # [0,0,0,0]

        for i in range(n):
            # go left to right for i and same time do righ to left for j
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult = l_mult * nums[i]
            r_mult = r_mult * nums[j]
        
        return [l*r for l,r in zip(l_arr,r_arr)]


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))



# O(n^2) solution / brute force, use i and j pointers
        # res = []
        # i = 0

        # while i < len(nums):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product = product * nums[j]
        #     res.append(product)
        #     i = i + 1
        # return res