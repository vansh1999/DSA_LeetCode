import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # arr = []
        
        # for i in range(n**31):
        #     arr.append(2**i)

        # if n in arr:
        #     return True
        # else:
        #     return False

        
        # time -> O(1)

        ### power of 3 solution
        
        if n == 0:
            return False
        if n < 0:
            return False

        while n%3 ==0:
            n = n//3
        
        if n == 1:
            return True
        
        return False
    
sol  = Solution()
print(sol.isPowerOfTwo(14))