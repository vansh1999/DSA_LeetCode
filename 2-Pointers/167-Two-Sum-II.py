class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Own code - Run , but failed due to time - code and logic is correct

        # for i in range(len(numbers)):

        #     for j in range(i+1 , len(numbers)):

        #         if numbers[i] + numbers[j] == target:
        #             return [i+1 , j+1]


        l = 0
        r = len(numbers) - 1

        while l < r:

            current = numbers[l] + numbers[r]

            if current == target:
                return [l+1 , r+1]
            
            elif target > current:
                l = l + 1 
            
            elif target < current:
                r = r - 1
                


sol = Solution()
print(sol.twoSum([2,7,11,15] , 9))