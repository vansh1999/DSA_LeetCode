class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
# Time -> O(2^n)
# Space -> O(n) why ? maximum extra memory used at any point during execution

sol = Solution()
print(sol.fib(100))