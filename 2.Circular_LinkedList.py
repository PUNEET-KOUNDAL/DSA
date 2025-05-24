class Node :
    def __init__(self,value) :
        self.value = value
        self.next = None 


class LinkedList :
    def __init__(self) :
        self.head = None 
        self.tail = None

    def __str__(self):
        if self.head is None:
            return "Circular Linked List is empty"
        temp_node = self.head
        result = ''
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' --> '
        return result
    

    def create(self , value ) :
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node

        return 'cicular linked list is created'
    
    def prepend(self , value) :
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else :
            new_node.next = self.head
            self.haed = new_node 
            self.tail = new_node

    def append(self , value) :
        new_node = Node(value) 
        if self.head is None :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else :
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def insert(self,index,value) :
        pass

    

            
            