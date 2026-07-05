class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # own code -> Time -> O(n)

        stack = []

        for i in tokens:

            if i not in ["+" , "-" , "*" , "/"]:
                stack.append(int(i))
            elif i == "+":
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i == "*":
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i == "/":
                res = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(res))

        return stack[0]


sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))