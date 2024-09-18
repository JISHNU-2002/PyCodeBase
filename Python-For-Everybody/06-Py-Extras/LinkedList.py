class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def insertFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertBack(self, data):
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        
    def insertPosition(self, data, pos):
        if pos == 0:
            self.insertFront(data)
            return 
        
        new_node = Node(data)
        
        ptr = self.head
        for i in range(1, pos):
            if ptr is None:
                print('IndexOutOfBound')
                return  
            ptr = ptr.next
            
        if ptr is None:
            print('IndexOutOfBound')
            return
        
        new_node.next = ptr.next
        ptr.next = new_node
            
    def deleteFront(self):
        if self.isEmpty():
            print('Underflow')
            return
        self.head = self.head.next
        
    def deleteBack(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        if self.head.next is None:
            print('Only node in list is deleted')
            self.head = None
            return
        
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None
        
    def deleteAtPosition(self, pos):
        if self.isEmpty():
            print('Underflow')
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        ptr = self.head
        for i in range(1, pos):
            if ptr.next is None:
                print('IndexOutOfBound')
                return
            ptr = ptr.next
            
        if ptr.next is None:
            print('IndexOutOfBound')
            return
        
        ptr.next = ptr.next.next
        
    def deleteFirstOccurence(self, value):
        if self.isEmpty():
            print('Underflow')
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        ptr = self.head
        while ptr.next:
            if ptr.next.data == value:
                ptr.next = ptr.next.next
                return
            ptr = ptr.next
        print('Value not found in list')

    def deleteLastOccurence(self, value):
        if self.isEmpty():
            print('Underflow')
            return

        last_occurrence = None
        prev = None
        ptr = self.head
        
        while ptr:
            if ptr.data == value:
                last_occurrence = ptr
                prev = prev if last_occurrence else None
            prev = ptr
            ptr = ptr.next

        if not last_occurrence:
            print('Value not found in list')
            return

        if last_occurrence == self.head:
            self.head = self.head.next
        else:
            prev.next = last_occurrence.next


    def deleteAllOccurence(self, value):
        if self.isEmpty():
            print('Underflow')
            return
        
        while self.head and self.head.data == value:
            self.head = self.head.next
        
        ptr = self.head
        while ptr and ptr.next:
            if ptr.next.data == value:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        
        if self.isEmpty():
            print('List is empty after deletion')
        elif ptr is None or ptr.next is None:
            print('Value not found in list')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display(self):
        if self.isEmpty():
            print('Underflow') 
        
        ptr = self.head
        nodes = []
        
        while ptr:
            nodes.append(ptr.data)
            ptr = ptr.next
        print(nodes)  


obj = LinkedList()

obj.insertFront(1)
obj.insertBack(2)
obj.insertFront(-1)
obj.insertBack(3)
obj.insertFront(-2)
obj.display()  
obj.insertPosition(0, 2)
obj.display()  
obj.deleteFront()
obj.display()  
obj.deleteBack()
obj.display()  
obj.deleteAtPosition(1)
obj.display()  
obj.reverse()
obj.display()  
obj.deleteAtPosition(2)
obj.display()  
obj.insertBack(2)
obj.display()  
obj.deleteValue(2)
obj.display()  