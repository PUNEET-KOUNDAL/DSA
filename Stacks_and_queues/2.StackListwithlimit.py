class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        value = self.list[::-1]  # Reverse the list for stack view
        value = [str(x) for x in value]
        return "\n".join(value)

    def isempty(self):
        if len(self.list) == 0 :
            return True 
        return len(self.list) , (self.maxsize)

    def isfull(self):
        return len(self.list) == self.maxsize

    def append(self, value):
        if self.isfull():
            return "Stack Overflow! Cannot add more elements."
        self.list.append(value)
        return "Element added successfully!"
    

        # Pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    

        # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
    
        #  delete
    def delete(self):
        self.list = None



