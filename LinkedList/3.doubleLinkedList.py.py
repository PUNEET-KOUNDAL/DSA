class Node :
    def __init__(self,value) :
        self.value = value 
        self.next = None 
        self.prev = None 

class DoubleLinkedList :
    def __init__(self,value ) :
        self.head = None
        self.tail = None
        self.length = None 

        if value is not None :
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length =  1


    def __str__(self) :
        temp = self.head 
        result = ' '
        while temp :
            result += str(temp.value)
            temp = temp.next
            if temp.next is not None :
                result += '< - >'

        return result 
    
    def append(self ,value ) :
        new_node = Node(value) 
        if self.head is None :
            self.head  = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


    def append(self,value ) :
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.append += 1


    def traverse(self) :
        current_node = self.head 
        result = ' '
        while current_node :
            result += str(current_node.value)
            if current_node.next is not None :
                result += ' < - >' 

            current_node = current_node.next
            
        return result
    

    def reverse(self) :
        current_node = self.tail 
        result = ' '
        while current_node :
            result = str(current_node.value)
            if current_node.next :
                result += ' < - >'

            current_node = current_node.next


        return result
    

    def search(self , target ) :
        current_node = self.head  # Start from the head
        while current_node:
            if current_node.value == target:  # If the target is found
                return current_node  # Return the node containing the target
            current_node = current_node.next  # Move to the next node
        return None  
    
    def get(self,index ) :
        if index < 0 and index >= self.length:
            return None 
        if index < self.length // 2 :
            current_node = self.head 
            for _ in range (index) :
                current_node = current_node.next
        else :
            current_node = self.tail 
            for _ in range (self.length - 1 , index , -1) :
                current_node = current_node.prev

        return current_node
    
    def set (self , index , value) :
        current_node = self.get(index)
        if current_node :
            current_node.vlaue = value
            return "value is set"
        return 'invalid index'
    

    def insert(self, index, value):
        if index < 0 or index > self.length:  # Validate index
            return "Invalid index"
        
        new_node = Node(value)  # Create a new node with the given value
        if index == 0:  # If inserting at the beginning
            self.prepend(value)
            return "Node inserted at the beginning."
        
        if index == self.length:  # If inserting at the end
            self.append(value)
            return "Node inserted at the end."
        
        temp_node = self.get(index - 1)
        if not temp_node :
            return 'node inserted at the end'
        
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        return 'node insert sucessfully'

    def pop_first(self):
        if not self.head:  # If the list is empty
            return None  
        
        popped_node = self.head  # Store the head node to return later
        if self.length == 1:  # If there's only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next  # Move the head to the next node
            self.head.prev = None  # Set the new head's prev to None
            popped_node.next = None  # Disconnect the old head from the list
        self.length -= 1  # Decrement the list length
        return popped_node  # Return the popped node
    



    def pop(self):
        if not self.head:  # If the list is empty
            return None
        
        popped_node = self.tail  # Store the tail node to return later
        if self.length == 1:  # If there's only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # Move the tail to the previous node
            self.tail.next = None  # Disconnect the old tail from the list
        popped_node.prev = None  # Disconnect the popped node from the list
        popped_node.next = None
        self.length -= 1  # Decrement the list length
        return popped_node  # Return the popped node
    


    def remove(self, index):
        if index < 0 or index >= self.length:  # Validate index
            return "Invalid index"
        
        if index == 0:  # If removing the first node
            return self.pop_first()
        
        if index == self.length - 1:  # If removing the last node
            return self.pop()

        popped_node = self.get(index)  # Get the node at the specified index
        popped_node.prev.next = popped_node.next  # Update the previous node's next
        popped_node.next.prev = popped_node.prev  # Update the next node's prev
        popped_node.next = None  # Disconnect the popped node from the list
        popped_node.prev = None
        self.length -= 1  # Decrement the list length
        return popped_node  # Return the popped node

    def delete(self):
        if self.head is None:  # If the list is already empty
            print("The list is already empty.")
        else:
            current_node = self.head
            while current_node:  # Traverse the entire list
                current_node.prev = None  # Disconnect the prev pointer of each node
                current_node = current_node.next  # Move to the next node

        self.head = None  # Set head to None
        self.tail = None  # Set tail to None
        self.length = 0  # Reset the length
        print("The list has been deleted.")  # Print a message when the list is deleted

    
