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

    def insert(yoo, index, value):
        new_node = Node(value)
        if yoo.head is None:  # Case 1: Empty list
            yoo.head = new_node
            yoo.tail = new_node
            new_node.next = new_node  # Points to itself
        elif index == 0:  # Case 2: Insert at the beginning
            new_node.next = yoo.head
            yoo.head = new_node
            yoo.tail.next = new_node  # Maintain circular link
        elif index >= yoo.length():  # Insert at the end
            yoo.append(value)
        else:  # Insert at a specific position
            temp_node = yoo.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def length(yoo):
        if yoo.head is None:
            return 0
        temp_node = yoo.head
        count = 0
        while True:
            count += 1
            temp_node = temp_node.next
            if temp_node == yoo.head:
                break
        return count
    
    def tansversal(yoo):
        temp_node = yoo.head
        while temp_node :
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == yoo.head:
                break
    
    def search(yoo, target):
        if yoo.head is None :
            return False
        temp_node = yoo.head
        index=0
        while True  :
            if temp_node.value == target :
                return "7 crore", index
            temp_node = temp_node.next
            index += 1
            if temp_node == yoo.head:
                break
        return "teri maa chord  kar gayi thi  yeh phir tera baap"
    

    def get(yoo,index):
        if yoo.head is None:
            return "htt"
        temp_node = yoo.head
        fake_index = 0 
        while temp_node is not None :
            if fake_index == index :
                return temp_node
            temp_node = temp_node.next
            fake_index +=1 
            if temp_node == yoo.head:
                break
        
        return "bhai tu kahi or dundh"
    
    def set(yoo, index, value):

        temp = yoo.get(index)

        temp.value = value
        return True
       

    def popfirst(yoo):
        if yoo.head is None:
            return "tera pyar ki tarah ye bi khali hai "
        
        if yoo.head.next == yoo.head:
            pop_value = yoo.head.value
            yoo.head = None 
            return pop_value
        

        pop_value = yoo.head.value
        yoo.head=yoo.head.next
        temp=yoo.head
        while temp.next != yoo.head:
            temp = temp.next 
        temp.next = yoo.head 
        return pop_value
    

    #pop
    #pop
    #insert

    
    def remove(self,index):
        if index < 0 or index > self.length :
            return 'invalid index'
        if index == 0 :
            return self.popfirst
        if index == self.length-1:
            return self.pop
        prev_node = self.get(index -1)
        pop_node = prev_node.next
        prev_node.next = pop_node.next
        pop_node.next = None
        self.length -= 1
        







    def delete_all(yoo):
        yoo.tail.next = None  # Breaking the circular link
        yoo.head = None
        yoo.tail = None
        return "sucessfull"
