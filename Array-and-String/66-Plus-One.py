class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits) - 1

        while n >= 0:

            # if last is not 9, simply add 1
            if digits[n] != 9:

                digits[n] = digits[n] + 1
                return digits
            
            # keep adding 0 and carry 1 in next non 9
            else:
                digits[n] = 0
                n = n - 1

        # if reached here, means all were 9, simply add 1 to first position
        digits.insert(0,1)
        # return new digit
        return digits

        
              
sol = Solution()
print(sol.plusOne([9,9]))