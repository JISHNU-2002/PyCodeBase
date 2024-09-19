class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def insertFront(self):
        data = int(input('\nEnter value : '))
        new_node = Node(data)
        new_node.next = self.head
        
        if not self.isEmpty():
            self.head.prev = new_node
            
        self.head = new_node
        self.display()
        
    def insertBack(self):
        data = int(input('\nEnter value : '))
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        new_node.prev = ptr
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
            if ptr is None:
                print('IndexOutOfBound')
                return
            ptr = ptr.next
            
        if ptr is None:
            print('IndexOutOfBound')
            return 
        
        data = int(input('\nEnter value : '))
        new_node = Node(data)
        
        new_node.next = ptr.next
        if ptr.next is not None:
            ptr.next.prev = new_node
            
        ptr.next = new_node
        new_node.prev = ptr
        self.display()
        
    def deleteFront(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        self.head = self.head.next
        self.display()
        
    def deleteBack(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        if self.head.next is not None:
            self.head = None
            print('Only node in list is deleted')
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.prev.next = None
        self.display()
        
    def deleteAtPosition(self):
        if self.isEmpty():
            print('Underflow')
            return
        
    def deleteFirstOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
        
    def deleteLastOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
        
    def deleteAllOccurrences(self):
        if self.isEmpty():
            print('Underflow')
            return
        
    def emptyList(self):
        self.head = None
        self.display()
        print('List is Empty')
        
    def reverse(self):
        if self.isEmpty():
            print('Underflow')
            return
        
    def display(self):
        if self.isEmpty():
            print('Underflow')
        
        ptr = self.head
        nodes = []
        while ptr:
            nodes.append(ptr.data)
            ptr = ptr.next
        print(nodes)
            
        
def main():
    obj = DoublyLinkedList()
    while True:
        print("\n\
        Doubly Linked List Operations\n\
        -----------------------------\n\
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
