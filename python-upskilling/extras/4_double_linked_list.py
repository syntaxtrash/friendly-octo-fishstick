class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
    
    def delete_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                if current == self.head:
                    self.head = current.next_node
                if current == self.tail:
                    self.tail = current.prev_node
                return True
            current = current.next_node
        return False
    
    def insert_after(self, existing_value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == existing_value:
                new_node.prev_node = current
                new_node.next_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = new_node
                current.next_node = new_node
                if current == self.tail:
                    self.tail = new_node
                return True
            current = current.next_node
        return False
    
    def insert_before(self, existing_value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == existing_value:
                new_node.prev_node = current.prev_node
                new_node.next_node = current
                if current.prev_node:
                    current.prev_node.next_node = new_node
                else:
                    self.head = new_node
                current.prev_node = new_node
                return True
            current = current.next_node
        return False
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node

# Create list
dll = DoublyLinkedList()

# Add nodes
dll.add_node("A")
dll.add_node("B")
dll.add_node("C")

print("Initial list:")
dll.print_list()

# Delete a node
dll.delete_node("B")

print("\nAfter deleting 'B':")
dll.print_list()

# Insert after a node
dll.insert_after("A", "D")

print("\nAfter inserting 'D' after 'A':")
dll.print_list()

# Insert before a node
dll.insert_before("C", "E")

print("\nAfter inserting 'E' before 'C':")
dll.print_list()
