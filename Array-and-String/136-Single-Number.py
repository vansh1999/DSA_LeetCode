class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # own brute force
        # time -> O(n^2) - passed
        # space -> O(n) - failed to do in O(1)

        # arr = []

        # for i in nums:

        #     if i not in arr:
        #         arr.append(i)
        #     else:
        #         arr.remove(i)

        # return arr[0]
        
        # can do via hashmaps -> O(n) time
        # but O(1) -> still fails

        s = set()

        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        
        return s.pop()
    
        # OR
        # return list(s)[0]


        # for O(n) and O(1) - XOR


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))