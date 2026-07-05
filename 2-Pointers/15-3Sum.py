class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Sort the arr first
        nums.sort()

        answer = []

        n = len(nums)

        for i in range(n):

            # if i is > 0, it will never be 0 break it
            if nums[i] > 0:
                break

            # skip the same number
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            # already have i -> take low and high and squeeze them
            low , high = i + 1, n - 1
            while low < high:

                sum = nums[i] + nums[low] + nums[high]

                if sum == 0:
                    answer.append([nums[i] , nums[low] , nums[high]])
                    low, high = low+1 , high-1

                    while low < high and nums[low] == nums[low-1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high+1]:
                        high = high - 1
                
                elif sum < 0:
                    low = low + 1

                else:
                    high = high - 1

            
        return answer


# time -> O(nlog n) + O(n^2) -> O(n^2)
# Space -> O(1) or O(n) -> based on programming lang
        



sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))