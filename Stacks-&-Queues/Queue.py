class Node:

    def __init__(self , value, next=None):
        self.value = value
        self.next = next

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    # Add (Enque) - O(1)

    def add(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    # Remove (Dequeue) - O(1)

    def remove(self):

        if self.head is None:
            return None

        removed = self.head.value

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed
    
    # Search - O(n)

    def search(self , value):

        current  = self.head

        while current:
            if current.value == value:
                return True
            
            current = current.next
        
        return False