class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        counter = {}

        word = "balon"

        for c in text:
            if c not in counter and c in word:
                counter[c] = 1
            elif c in counter and c in word:
                counter[c] = counter[c] + 1

        # return counter

        # dict.get(key, default) -> what is key value, if not 0. since my counter has keys which are in balon, i can skip 0. now get the min which need to create balloon. which is 1 b , 1 a, 2 l, 2 o, and 1 n
        # but need 0, what if balon never exists in text

        # imp

        b = counter.get('b' , 0)
        a = counter.get('a' , 0)
        l = counter.get('l' , 0) // 2
        o = counter.get('o' , 0) // 2
        n = counter.get('n' , 0) 

        return min(b,a,l,o,n)

        

sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))