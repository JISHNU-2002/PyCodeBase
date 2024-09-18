class Node():
    def __init__(self):
        self.prev = None
        self.data = None
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
        self.head.prev = new_node
        self.head = new_node
        print(f'{data} inserted at front')
        
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
        print(f'{data} inserted at back')
        
    def insertAtPosition(self):
        data = int(input('\nEnter value : '))
        pos = int(input('\nEnter position : '))
        new_node = Node(data)
        
        if pos == 0:
            self.insertFront()
            
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
        new_node.prev = ptr
        print(f'{data} inserted at position {pos}')
        
    def display(self):
        if self.isEmpty():
            print('Underflow')
            
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
        10. Reverse the list\n\
        11. Display\n\
        12. Exit\n")
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
            10: obj.reverse,
            11: obj.display,
            12: exit
        }
        func = switch.get(choice, lambda: print("Please enter a valid choice."))
        func()

if __name__ == "__main__":
    main()
