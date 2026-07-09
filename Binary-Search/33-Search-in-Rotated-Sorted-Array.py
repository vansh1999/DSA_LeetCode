class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Brute Force - O(n)

        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == target:
        #         return i
        
        # return -1

        # M2 - Checks which half is sorted and search using binary search - O(log n)

        n = len(nums)
        l = 0 
        r = n-1


        while l<=r:
            mid = (l+r) //2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                # left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else:
                # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
        

# time - O(logn)

sol = Solution()
print(sol.search([1] , 0))