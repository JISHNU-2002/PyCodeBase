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
            self.display()
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
        
        if self.head.next is None:
            self.head = None
            print('Only node in list is deleted')
            return
        
        self.head = self.head.next
        self.display()
        
    def deleteBack(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        if self.head.next is None:
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
        
        pos = int(input('\nEnter the position : '))
        if pos<0:
            print('Enter a valid position')
            return
        
        if pos == 0:
            self.deleteFront()
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
        if ptr.next is not None:
            ptr.next.prev = ptr
        self.display()
    
    def deleteFirstOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        value = int(input("\nEnter value : "))
        ptr = self.head
        
        while ptr:
            if ptr.data == value:
                if ptr.prev is not None:
                    ptr.prev.next = ptr.next
                if ptr.next is not None:
                    ptr.next.prev = ptr.prev
                if ptr == self.head:
                    self.head = self.head.next
                self.display()
                return
            ptr = ptr.next
        print(f'{value} not present in list')
        
    def deleteLastOccurrence(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        value = int(input("\nEnter value : "))
        last_occurence = None
        ptr = self.head
        
        while ptr:
            if ptr.data == value:
                last_occurence = ptr
            ptr = ptr.next
        
        if last_occurence is None:
            print(f'{value} not present in list')
            return 
        
        if last_occurence.prev is not None:
            last_occurence.prev.next = last_occurence.next
        if last_occurence.next is not None:
            last_occurence.next.prev = last_occurence.prev
        if last_occurence == self.head:
            self.head = self.head.next
        self.display()
        
    def deleteAllOccurrences(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        value = int(input("\nEnter value : "))
        ptr = self.head
        found = False
        
        while ptr:
            if ptr.data == value:
                if ptr.prev is not None:
                    ptr.prev.next = ptr.next
                if ptr.next is not None:
                    ptr.next.prev = ptr.prev
                if ptr == self.head:
                    self.head = self.head.next
                found = True
            ptr = ptr.next
            
        if not found:
            print(f'{value} not present in list')
        else: self.display()
        
    def emptyList(self):
        self.head = None
        self.display()
        print('List is Empty')
        
    def reverse(self):
        if self.isEmpty():
            print('Underflow')
            return
        
        current = self.head
        prev = None
        
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        # After the loop, prev points to the old head's previous node
        if prev:
            self.head = prev.prev
        
        self.display()

        
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
