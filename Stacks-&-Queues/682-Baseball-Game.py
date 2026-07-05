class Solution:
    def calPoints(self, operations: List[str]) -> int:


        # 1 -> Int -> append to list / R
        # 2 -> + -> sum [i-1] + [i-2]
        # 3 -> D -> [i-1] * 2
        # 4 -> C -> pop / R

        res = []

        for i in operations:
            print(i)

            if i not in ["+" , "D" , "C"]:
                res.append(int(i))

            elif i == "+":
                sum = res[-1] + res[-2]
                res.append(sum)

            elif i == "D":
                dbl = res[-1] * 2
                res.append(dbl)
            
            elif i == "C":
                res.pop()
            
   

        # print(res)
        sum = 0
        for i in range(len(res)):
            sum = res[i] + sum

        return sum
    

        # time -> O(n)
        # space -> O(n)
        


sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))