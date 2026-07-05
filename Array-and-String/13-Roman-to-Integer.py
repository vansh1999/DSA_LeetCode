# I -> 1
# V -> 5
# X -> 10

class Solution:
    def romanToInt(self, s: str) -> int:

        # validate 
        # count = 1
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         count = count+1
        #         if s[i] in ["I", "X", "C"] and count > 3:
        #             return 0

        # Roman to interger
        num = 0
        i =0

        while i < len(s):

            if i < len(s)-1 and s[i] == "I" and s[i+1] == "V":
                num = num + 4
                i = i+2
            elif i < len(s)-1 and s[i] == "I" and s[i+1] == "X":
                num = num + 9
                i = i+2
            elif i < len(s) - 1 and s[i] == "X" and s[i + 1] == "L":
                num += 40
                i =i+2
            elif i < len(s) - 1 and s[i] == "X" and s[i + 1] == "C":
                num += 90
                i += 2
            elif i < len(s) - 1 and s[i] == "C" and s[i + 1] == "D":
                num += 400
                i += 2
            elif i < len(s) - 1 and s[i] == "C" and s[i + 1] == "M":
                num += 900
                i += 2
            
            elif s[i] == "I":
                num = num + 1
                i = i+1
            elif s[i] == "V":
                num = num + 5
                i = i+1
            elif s[i] == "X":
                num = num + 10
                i = i+1
            elif s[i] == "L":
                num += 50
                i += 1
            elif s[i] == "C":
                num += 100
                i += 1
            elif s[i] == "D":
                num += 500
                i += 1
            elif s[i] == "M":
                num += 1000
                i += 1

        return num

sol = Solution()
print(sol.romanToInt("MCMXCIV"))

# Time Complexity: O(n), because we traverse the Roman numeral string once.

# Space Complexity: O(1), because we use only a constant amount of extra memory regardless of input size.

# later -> do with hash map {'I':1 , 'V':5}