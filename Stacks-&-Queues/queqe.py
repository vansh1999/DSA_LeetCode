# Queue (FIFO - First In First Out)

from  collections import deque

# Internally, a deque (double-ended queue) is optimized for fast insertions and removals at both ends.
queue = deque()


# Enqueue (Add right) - Add elements to the right - O(1)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Dequeue (Pop Left) - Remove the element from the left - O(1) [Implemented as doubly linkedList]

queue.popleft()

print(queue)

# Peek from the left side - O(1)

# first to pop out from queue
print(queue[0])

# last in queue to pop out
print(queue[-1])


# keywords 
# deque() → the data structure (double ended queue implemented in python)
# Enqueue -> insert element into the queue (R)
# Dequeue -> remove element (L)

# implemented Queue from Scratch in Queue.py