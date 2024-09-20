class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
class CircularLinkedList():
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def insertFront(self):
        data = int(input('\nEnter the value : '))
        new_node = Node(data)
        
        if self.isEmpty():
            new_node.prev = new_node.next = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = tail.next = new_node
            self.head = new_node
        self.display()  
        
    def insertBack(self):
        data = int(input('\nEnter value : '))
        new_node = Node(data)
        
        if self.isEmpty():
            new_node.prev = new_node.next = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = tail.next = new_node
        self.display()
        
    def insertAtPosition(self):
        pos = int(input('\nEnter position : '))
        if pos<0:
            print('Enter a valid position')
            return
        
        if pos == 0:
            self.insertFront()
            return
        
        ptr = self.head
        for i in range(1, pos):
            ptr = ptr.next
            if ptr == self.head:
                print('IndexOutOfBound')
                return
            
        data = int(input('Enter value : '))
        new_node = Node(data)
        
        new_node.next = ptr.next
        new_node.prev = ptr
        ptr.next.prev = new_node
        ptr.next = new_node
        self.display()
        
    def deleteFront(self):
        if self.isEmpty():
            print('Underflow')
        elif self.head.next == self.head:
            self.head = None
            print('Only node in list deleted')
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head
            self.display()
            
    def deleteBack(self):
        if self.isEmpty():
            print('Underflow')
        elif self.head.next == self.head:
            self.head = None
            print('Only node in list deleted')
        else:
            tail = self.head.prev
            tail.prev.next = self.head
            self.head.prev = tail.prev
            self.display()
            
    def deleteAtPosition(self):
        if self.isEmpty():
            print('Underflow')
            
        pos = int(input('\nEnter position : '))
        if pos<0:
            print('Enter a valid position')
            return
        if pos == 0:
            self.deleteFront()
            return
        
        ptr = self.head
        for i in range(1, pos):
            ptr = ptr.next
            if ptr == self.head:
                print('IndexOutOfBound')
                return

        if ptr.next == self.head:
            print('IndexOutOfBound')
            return 
        
        node = ptr.next
        ptr.next = node.next
        node.next.prev = ptr
        self.display()
        
    def deleteFirstOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
            
        value = int(input('\nEnter value : '))
        if self.head.data == value:
            self.deleteFront()
            return
        
        ptr = self.head.next
        while ptr != self.head:
            if ptr.data == value:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
                self.display()
                return
            ptr = ptr.next
        print(f'{value} not present in list')
        
    def deleteLastOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
            
        value = int(input('\nEnter value : '))
        last_occurence = None
        
        ptr = self.head
        while ptr:
            if ptr.data == value:
                last_occurence = ptr
            ptr = ptr.next
            if ptr == self.head:
                break
        
        if last_occurence == self.head:
            self.deleteFront()
            return
        if last_occurence is None:
            print(f'{value} not present in list')
            return
    
        last_occurence.prev.next = last_occurence.next
        last_occurence.next.prev = last_occurence.prev
        self.display()
        
    def deleteAllOccurrences(self):
        if self.isEmpty():
            print('Underflow')
            return
            
        value = int(input('\nEnter value : '))
        ptr = self.head
        found = False
        
        while ptr:
            if ptr.data == value:
                if ptr == self.head:
                    self.deleteFront()
            ptr = ptr.next
            
            if ptr == self.head:
                break
    
    def reverse(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        current = self.head
        tail = self.head.prev
        
        while True:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            
            if current.prev == self.head:
                break
            
            current = current.prev
        self.head = tail
        self.display()
    
    def emptyList(self):
        self.head = None
        self.display()
        print('List is Empty')

        
    def display(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        ptr = self.head
        nodes = []
        while ptr:
            nodes.append(ptr.data)
            ptr = ptr.next
            if ptr == self.head:
                break
        print(nodes)
            
def main():
    obj = CircularLinkedList()
    while True:
        print("\n\
        Circular Linked List Operations\n\
        -------------------------------\n\
        1. Insert in beginning\n\
        2. Insert at last\n\
        3. Insert at any random location\n\
        4. Delete from beginning\n\
        5. Delete from last\n\
        6. Delete node from specified location\n\
        7. Delete first Occurrence of a Value\n\
        8. Delete last Occurrence of a Value\n\
        9. Delete all Occurrence of a Value\n\
        10. Empty the List\n\
        11. Reverse the list\n\
        12. Display\n\
        13. Exit\n")
        choice = int(input("Enter your choice : "))

        switch = {
            1: obj.insertFront,
            2: obj.insertBack,
            3: obj.insertAtPosition,
            4: obj.deleteFront,
            5: obj.deleteBack,
            6: obj.deleteAtPosition,
            7: obj.deleteFirstOccurrence,
            8: obj.deleteLastOccurrence,
            9: obj.deleteAllOccurrences,
            10: obj.emptyList,
            11: obj.reverse,
            12: obj.display,
            13: exit
        }
        func = switch.get(choice, lambda: print("Please enter a valid choice"))
        func()

if __name__ == "__main__":
    main()
