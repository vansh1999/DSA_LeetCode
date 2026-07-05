class Solution:
    def isValid(self, s: str) -> bool:

        # to add and remove parantheses for validation
        stack = []

        # hashmap for lookup
        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # for c in s:
        #     if c in hashmap:
        #         # is closing
        #         if not stack or stack[-1] != hashmap[c]:
        #             return False
                
        #         # if same, need to remove 
        #         stack.pop()

        #     else:
        #         stack.append(c)

        for c in s:

            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != hashmap[c]:
                    return False
                stack.pop()


        if stack:
            return False
        else:
            return True
        

sol = Solution()
print(sol.isValid("([])"))