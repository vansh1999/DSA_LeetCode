class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # my solution -> using mashmap

        # counter = {}

        # for c in nums:

        #     if c in counter:
        #         counter[c] = counter[c] + 1

        #         if counter[c] > 1:
        #             return True
            
        #     else:
        #         counter[c] = 1
        
        # return False


        counter = {}
    
        # i is index here in range(len(nums))
        # when we do i in nums , i is value

        # for i in range(len(nums)):
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] = counter[i] + 1
                return True
        
        return False
            
    
    # return counter
    
    # return False

        # using -> hashsets

        # n = set()

        # for i in nums:

        #     if i in n:
        #         return True
        #     else:
        #         n.add(i)
        
        # return False
    

    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
        