class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        # find min times to check pointer 
        min_len = float('inf')
        for n in strs:
            if len(n) < min_len:
                min_len = len(n)
        
        i = 0

        # get prefix till anything mismatches
        # iterate - flower flow flight
        # check each elements against flower till not match, and get whatever matched
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i = i + 1

        return strs[0][:i]


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))