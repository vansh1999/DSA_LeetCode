class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0
        sub_str = ""

        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                sub_str = sub_str + s[i]
                print(sub_str)
                i = i + 1
                j = j + 1
            else:
                j = j + 1

        if sub_str == s:
            return True
        else:
            return False


sol = Solution()
print(sol.isSubsequence("abc" , "ahbgdc"))

# implemented using two pointer
# time -> O(n+m^2)
# space -> O(n)