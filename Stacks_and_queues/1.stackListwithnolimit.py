class Stack:
    """
    A simple implementation of a stack (LIFO: Last-In, First-Out) using a Python list.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.list = []

    def __str__(self):
        """
        Returns a string representation of the stack from top to bottom.
        """
        value = self.list[::-1]  # Display from top (end of list) to bottom
        return "\n".join(str(x) for x in value)

    def push(self, value):
        """
        Pushes an element onto the stack.

        Parameters:
        value (any): The value to be pushed onto the stack.

        Returns:
        str: Confirmation message.
        """
        self.list.append(value)
        return "Element pushed successfully!"

    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
        bool: True if empty, False otherwise.
        """
        return len(self.list) == 0

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
        any: The popped element or an error message if the stack is empty.
        """
        if self.isEmpty():
            return "Stack is empty!"
        return self.list.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
        any: The top element or a message if the stack is empty.
        """
        if self.isEmpty():
            return "Stack is empty!"
        return self.list[-1]

    def delete(self):
        """
        Deletes all elements from the stack.

        Returns:
        str: Message indicating whether the stack was cleared or already empty.
        """
        if self.isEmpty():
            return "Stack is already empty!"
        self.list = []
        return "Stack deleted successfully!"
