class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head is None:
            return self.add_to_front(val)
        new_node = SLNode(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if self.head is None:
            return None
        if self.head.value == val:
            return self.remove_from_front()
        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                removed_value = runner.next.value
                runner.next = runner.next.next
                return removed_value
            runner = runner.next
        return None

    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        new_node = SLNode(val)
        runner = self.head
        for runner_index in range(n - 1):
            if runner is None:
                return None  # pag out of range
            runner = runner.next
        new_node.next = runner.next
        runner.next = new_node
        return self

# chain
my_list = SList()
print("Original: ")
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
print("=================")

# remove_from_front
print("\nRemove from front:")
print("Removed:", my_list.remove_from_front())
print("Output: ")
my_list.print_values()
print("=================")

# remove_from_back
print("\nRemove from back:")
print("Removed:", my_list.remove_from_back())
print("Output: ")
my_list.print_values()
print("=================")

# remove_val
print("Original: ")
my_list.add_to_back("awesome").add_to_back("great").print_values()
print("\nRemove value 'are':")
print("Removed:", my_list.remove_val("are"))
my_list.print_values()
print("=================")

# insert_at
print("\nInsert 'new' at index 1:")
my_list.insert_at("new", 1).print_values()
