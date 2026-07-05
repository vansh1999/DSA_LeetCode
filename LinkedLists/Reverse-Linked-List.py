# Reverse linkedlist

# Create  a linked list
class SingleNode:

    def __init__(self, value, next=None):

        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
    
Head = SingleNode(1)
Node_1 = SingleNode(2)
Node_2 = SingleNode(3)
Node_3 = SingleNode(4)


Head.next = Node_1
Node_1.next = Node_2
Node_2.next = Node_3


# Print LinkedList in order 

curr = Head
LinkedLists = []


while curr:
    LinkedLists.append(str(curr.value))
    curr = curr.next

print('->'.join(LinkedLists))


# Print reverse linkedList

# M1 -> recursive method 
# M2 -> iterative and change the order of list (next) from start to end

curr = Head
prev = None

while curr:

    temp = curr.next
    # change order
    curr.next = prev
    prev = curr
    curr = temp

# print linkedList in reverse

Reverse_LinkedLists = []
# last iteration , Head is at prev
curr = prev

while curr:
    Reverse_LinkedLists.append(str(curr.value))
    curr = curr.next
print('->'.join(Reverse_LinkedLists))
