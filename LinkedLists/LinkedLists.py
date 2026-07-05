### Singly Linked List

class SingleNode:

    def __init__(self, value, next=None):

        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
    
Head = SingleNode(1)
Node_1 = SingleNode(3)
Node_2 = SingleNode(4)
Node_3 = SingleNode(7)

# till now nodes are floating around the space

Head.next = Node_1
Node_1.next = Node_2
Node_2.next = Node_3

# print(Head) -> 1

# Traverse the list -> going to each node -> O(n)

curr = Head

while curr:
    # print(curr)
    curr = curr.next


# Displaying the linkedList

def Display(Head):

    curr = Head
    elements = []

    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(' -> '.join(elements))

Display(Head)


# Search for a node Value - O(n)

def search(Head, value):

    curr = Head
    while curr:
        if value == curr.value:
            return True
        curr = curr.next

    return False
    
search(Head , 3)


