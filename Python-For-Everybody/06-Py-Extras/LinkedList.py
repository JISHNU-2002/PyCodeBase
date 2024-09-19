class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def insertFront(self):
        data = int(input("\nEnter value : "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()
        
    def insertBack(self):
        data = int(input("\nEnter value : "))
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        self.display()
        
    def insertAtPosition(self):
        pos = int(input("\nEnter position : "))
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
        
        data = int(input("\nEnter value : "))
        new_node = Node(data)
        
        new_node.next = ptr.next
        ptr.next = new_node
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
        
        if self.head.next is None:
            print('Only node in list is deleted')
            self.head = None
            return
        
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None
        self.display()
        
    def deleteAtPosition(self):
        pos = int(input("\nEnter position : "))
        if pos<0:
            print('Enter a valid position')
            return
        
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
        self.display()
        
    def deleteFirstOccurrence(self):
        value = int(input("\nEnter value : "))
        if self.isEmpty():
            print('Underflow')
            return
        
        if self.head.data == value:
            self.head = self.head.next
            self.display()
            return
        
        ptr = self.head
        while ptr.next:
            if ptr.next.data == value:
                ptr.next = ptr.next.next
                self.display()
                return
            ptr = ptr.next
        print(f'{value} not found in list')

    def deleteLastOccurrence(self):
        value = int(input("\nEnter value : "))
        if self.isEmpty():
            print('Underflow')
            return

        last_occurrence = None
        last_occurrence_prev = None
        ptr = self.head
        prev = None

        while ptr:
            if ptr.data == value:
                last_occurrence = ptr
                last_occurrence_prev = prev
            prev = ptr
            ptr = ptr.next

        if not last_occurrence:
            print(f'{value} not found in list')
            return

        if last_occurrence == self.head:
            self.head = self.head.next
            self.display()
        else:
            last_occurrence_prev.next = last_occurrence.next
            self.display()

    def deleteAllOccurrences(self):
        value = int(input("\nEnter value : "))
        if self.isEmpty():
            print('Underflow')
            return
        
        found = False
        while self.head and self.head.data == value:
            self.head = self.head.next
            found = True
        
        ptr = self.head
        while ptr and ptr.next:
            if ptr.next.data == value:
                ptr.next = ptr.next.next
                found = True
            else:
                ptr = ptr.next
        
        if not found:
            print(f'{value} not found in list')
        elif self.isEmpty():
            print('List is empty after deletion')
        else:
            self.display()
            print(f'All occurrences of {value} have been deleted')

    def emptyList(self):
        self.head = None
        self.display()
        print('List is Empty')
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
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
    obj = LinkedList()
    while True:
        print("\n\
        Linked List Operations\n\
        ----------------------\n\
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
