# leetcode - find-closest-number-to-zero

# my solution

# arr = [-4, -2, -1, 1,  4, 8]

# abs_arr =[]

# for i in arr:
#     i = abs(i)
#     abs_arr.append(i)

# abs_arr.sort()

# print(abs_arr)
# print(abs_arr[0])

# time comlexxity - O(n) + O(n logn) + O(1) = O(n logn)

# wrong answer -> [-100000,-100000] -> 



# Solution 2

class Solution:

    
	
    def findClosestNumber(self, nums: List[int]) -> int:

        closest = nums[0]

        for x in nums:
    	    if abs(x) < abs(closest):
    		    closest = x

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
             return closest

nums = [-4, -2, -1, 1,  4, 8]

sol = Solution()
print(sol.findClosestNumber(nums))

# time complexity - O(n) + O(n) = O(2n)	= O(n)





