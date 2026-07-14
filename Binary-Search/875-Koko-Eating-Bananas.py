import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # need to return -> k
        # k = min no of banana koko needs to eat / per hr < in h hrs.

        def min_k(k):
            min_hrs = 0

            for i in piles:
                min_hrs = min_hrs + math.ceil( i / k)

            return min_hrs <= h
        

        l = 1
        r = max(piles)

        while l < r:
            k = (l+r) // 2
            if min_k(k):
                r = k
            else:
                l = k + 1
        
        return l
    

sol = Solution()
print(sol.minEatingSpeed([3,6,7,11] , 8 ))


# Iteration 1 — while l < r: → 1 < 11 → True
# k = (1 + 11) // 2 = 6
# Call min_k(6) → jumps into the function, fresh scope, local k = 6:
# min_hrs = 0
# i=3  -> ceil(3/6)=1  -> min_hrs=1
# i=6  -> ceil(6/6)=1  -> min_hrs=2
# i=7  -> ceil(7/6)=2  -> min_hrs=4
# i=11 -> ceil(11/6)=2 -> min_hrs=6
# return 6 <= 8   ->  True
# Back at call site: if True: r = k → r = 6. (That local scope with k=6 is now gone.)

# Iteration 2 — while l < r: → 1 < 6 → True
# k = (1 + 6) // 2 = 3
# Call min_k(3) → brand new scope, local k = 3 (unrelated to the k=6 scope from before — that one no longer exists):
# min_hrs = 0
# i=3  -> ceil(3/3)=1  -> min_hrs=1
# i=6  -> ceil(6/3)=2  -> min_hrs=3
# i=7  -> ceil(7/3)=3  -> min_hrs=6
# i=11 -> ceil(11/3)=4 -> min_hrs=10
# return 10 <= 8   ->  False
# Back at call site: else: l = k + 1 → l = 4.

# Iteration 3 — while l < r: → 4 < 6 → True
# k = (4 + 6) // 2 = 5
# Call min_k(5) → new scope, local k = 5:
# min_hrs = 0
# i=3  -> ceil(3/5)=1  -> min_hrs=1
# i=6  -> ceil(6/5)=2  -> min_hrs=3
# i=7  -> ceil(7/5)=2  -> min_hrs=5
# i=11 -> ceil(11/5)=3 -> min_hrs=8
# return 8 <= 8   ->  True
# Back at call site: r = k → r = 5.

# Iteration 4 — while l < r: → 4 < 5 → True
# k = (4 + 5) // 2 = 4
# Call min_k(4) → new scope, local k = 4:
# min_hrs = 0
# i=3  -> ceil(3/4)=1  -> min_hrs=1
# i=6  -> ceil(6/4)=2  -> min_hrs=3
# i=7  -> ceil(7/4)=2  -> min_hrs=5
# i=11 -> ceil(11/4)=3 -> min_hrs=8
# return 8 <= 8   ->  True
# Back at call site: r = k → r = 4.

# Check loop condition again: while l < r: → 4 < 4 → False. Loop exits.
# return l   ->  4