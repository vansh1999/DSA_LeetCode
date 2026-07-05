class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # check how many stone in stones are also present in jewels

        # count = 0
        # for s in stones:
        #     if s in jewels:
        #         count = count + 1
        
        # return count
    
        # time complexity -> O(n * m)
        # n = len of stones
        # m = len of jewels

        # optimize jewels lookup from O(m) -> O(1) -> use hashset

        jewel_set = set(jewels)

        count = 0
        for s in stones:
            if s in jewel_set:
                count = count + 1
        return count
    
        # time complexity -> O(n+m)
        # n -> len of stones -> O(n)
        # each lookup in jewel_set = O(1)
        # total -> O(n+m)

