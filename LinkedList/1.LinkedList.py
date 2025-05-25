class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node in the list


class LinkedList:
    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list
        self.length = 0   # Number of nodes in the list

    def __str__(self):
        """Return a string representation of the linked list."""
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result += ' -> '
            temp = temp.next
        return result

    def append(self, value):
        """Add a node with `value` to the end of the list."""
        new_node = Node(value)
        if self.head is None:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link current tail to new node
            self.tail = new_node       # Update tail reference
        self.length += 1

    def prepend(self, value):
        """Add a node with `value` to the beginning of the list."""
        new_node = Node(value)
        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # New node points to old head
            self.head = new_node       # Update head reference
        self.length += 1

    def transversal(self):
        """Traverse and return string representation of the list."""
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def search(self, target):
        """Return the index of the first node with value == target or -1 if not found."""
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == target:
                return index
            index += 1
            temp_node = temp_node.next
        return -1

    def get(self, index):
        """Return the node at position `index` or 'error' if invalid."""
        if index < 0 or index >= self.length:
            return 'error'
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node

    def set_value(self, index, value):
        """Set the value of node at `index` to `value`. Return True if successful, else False."""
        if self.length == 0:
            return False
        temp_node = self.get(index)
        if temp_node != 'error' and temp_node is not None:
            temp_node.value = value
            return True
        return False

    def pop_first(self):
        """Remove and return the first node of the list."""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None  # Disconnect popped node from list
        self.length -= 1
        return popped_node

    def pop(self):
        """Remove and return the last node of the list."""
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            # Traverse to second last node
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None  # Disconnect last node
            self.tail = temp_node  # Update tail
        self.length -= 1
        return pop_node

    def removel(self, index):
        """Remove and return the node at a specific index."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        temp_node = self.get(index - 1)
        if temp_node == 'error' or temp_node is None:
            return None
        remove_node = temp_node.next
        temp_node.next = remove_node.next
        remove_node.next = None  # Disconnect removed node
        if index == self.length - 1:  # If last node removed, update tail
            self.tail = temp_node
        self.length -= 1
        return remove_node

    def delete(self):
        """Delete the entire linked list."""
        self.head = None
        self.tail = None
        self.length = 0
