class Solution:
    def findMin(self, nums: List[int]) -> int:

        # M1 - using brute force O(n)

        # find min

        # min = float('inf')

        # n = len(nums)

        # for i in range(n):
        #     if nums[i] < min:
        #         min = nums[i]

        # return min

        # M2 - use binary search to find first min, use L R and M - O(log n)

        n = len(nums)
        l = 0
        r = n-1

        # l < r
        while l<r:

            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l=mid+1
            else:
                r=mid
        
        return nums[l]
        # OR return nums[r] , since l == r


sol = Solution()
print(sol.findMin([-11,13,15,-100]))