# merge sorted array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        merged = []
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i = i+1
            else:
                merged.append(nums2[j])
                j = j+1
        
        while i < m:
            merged.append(nums1[i])
            i = i+1
        
        while j < n:
            merged.append(nums2[j])
            j = j+1


        # nums1 = merged / You only changed the function’s local variable. nums : -> Take every position in nums1 and replace its contents.
        nums1[:] = merged
        return nums1
    

sol = Solution()
print(sol.merge([1,2,3,0,0,0],3, [2,5,6],3))


