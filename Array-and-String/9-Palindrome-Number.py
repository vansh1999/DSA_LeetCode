class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if x < 0:
        #     return False

        # p = str(x)[::-1]

        # if int(p) == x:
        #     return True
        # else:
        #     return False
        

        # without ::-1 

        if x < 0:
            return False

        # to store reverse array
        answer = []

        # int to straight array of int
        arr = []
        for d in str(x):
            arr.append(int(d))

        n = len(arr)

        # reverse the array
        for i in range(n):
            answer.append(arr[n-1-i])

        # if stright array = reverse array -> true
        if arr == answer:
            return True
        else:
            return False
        

sol = Solution()
print(sol.isPalindrome(1201))