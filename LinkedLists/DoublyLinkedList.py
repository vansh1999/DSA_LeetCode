### Doubly Linked List

class DoublyNode:

    def __init__(self, value, next=None , prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

Head = Tail = DoublyNode(1)
# print(Tail)

# O(n)
def Display(Head):

    curr = Head
    elements = []

    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(' <-> '.join(elements))

# Display(Head)


# Insert at the beginning - O(1)

def insert_at_beginning(Head,Tail, value):
    new_node = DoublyNode(value , next=Head)
    Head.prev = new_node
    return new_node , Tail

Head , Tail = insert_at_beginning(Head , Tail , 3)
Display(Head)

# Insert at the end - O(1)
def insert_at_end(Head,Tail,value):
    new_node = DoublyNode(value,prev=Tail)
    Tail.next = new_node
    return Head , new_node

Head , Tail = insert_at_end(Head,Tail,7)
Display(Head)