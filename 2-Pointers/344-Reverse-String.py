class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # just reverse the string and return string
        # s.reverse()
        # return s

        # use 2 pointers L and R

        L = 0
        R = len(s) - 1

        while L <= R:
            s[L], s[R] = s[R] , s[L]
            L = L + 1
            R = R - 1
        
        # Time -> O(n)
        # Space -> O(1)

        
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))