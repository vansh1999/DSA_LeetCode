class Solution:
    def trap(self, height: List[int]) -> int:

# M1 -> using extra arr / prefix/suffix array / DP
# time complexity -> O(n) + O(n) + O(n) = O(3n) -> O(n)
# space -> O(2n)# prefix/suffix array / DP

        # n = len(height)

        # left_max = [0] * n
        # right_max = [0] * n

        # # build left max
        # left_max[0] = height[0]

        # for i in range(1,n):
        #     # prev max will be max, so compare prev max with this
        #     left_max[i] = max(left_max[i-1] , height[i])

        #     # Assume the previous maximum is still the answer
        #     # left_max[i] = left_max[i - 1]
        #     # Only update if the current building is taller
        #     # if height[i] > left_max[i]:
        #     #   left_max[i] = height[i] 


        # # build right max
        # right_max[n-1] = height[n-1]

        # for i in range(n-2 , -1 , -1):
        #     right_max[i] = max(right_max[i+1] , height[i])


        # # Calculate total water 

        # total_water = 0

        # for i in range(n):

        #     water = min(left_max[i] , right_max[i]) - height[i]
        #     total_water = total_water + water

        # return total_water
    


# M2 -> 2 Pointer
# Time -> O(n)
# Space -> O(1)
        if not height: return 0

        l,r = 0 , len(height) - 1
        l_max = height[l]
        r_max = height[r]

        res = 0

        while l < r:

            if l_max < r_max:
                l = l + 1
                l_max = max(l_max , height[l])
                res += l_max - height[l]

            else:
                r = r - 1
                r_max = max(r_max , height[r])
                res += r_max - height[r]
        
        return res


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))