class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # my solution - used brute force -> O(n^2)

        # days = []

        # n = len(temperatures)

        # for i in range(n-1):

        #     for j in range(i+1 , n):

        #         if temperatures[j] > temperatures[i]:
                    
        #             diff = j - i
        #             days.append(diff)
        #             # if greater temp is found, stop further checks in array
        #             break
            
        #     else:
        #          days.append(0)
                
        # # for last 
        # days.append(0)
            
        # return days


        # M2 -> use monotonic stack -> O(n)

        n = len(temperatures)

        answer = [0] * n 

        stack = []

        # enumerate() -> yields a tuple containing (index, item) on each iteration

        for i , t in enumerate(temperatures):

            # since we appended (t,i) -> (73,0)
            while stack and stack[-1][0] < t:

                stack_t , stack_i = stack.pop()
                answer[stack_i] = i - stack_i

            stack.append((t,i))


        return answer  
        
sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))