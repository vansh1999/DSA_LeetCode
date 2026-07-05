# Stack (LIFO - Last In First Out)

stack = []

print(stack)


# 1 Append to the stack (top) -> O(1)
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# 2 Pop from the stack (top) -> O(1)

x = stack.pop()

print(x)
print(stack)

# while using pop, keep in mind that something is in the stack, else error, so do -> if stack: true

# 3 Peek (lookup at top) -> O(1)

print(stack[-1])

# 4 Search in stack

i = 2
if i in stack:
    print(True)



