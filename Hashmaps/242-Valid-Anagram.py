class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # wrote on own

        counter = {}

        for c in s:
            if c in counter:
                counter[c] = counter[c] + 1
            elif c not in counter:
                counter[c] = 1
        
        for i in t:

            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else:
                counter[i] = counter[i] - 1
            
        # this is what is needed
        if len(counter) == 0:
            return True
        else:
            return False
                

sol = Solution()
print(sol.isAnagram("ab" , "a"))       


# t is anagram of s -> True 
# t not anagram of s else -> false 


# Time -> O(2n) -> O(n)