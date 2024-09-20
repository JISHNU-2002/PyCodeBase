class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

if __name__ == "__main__":
    root = None 

    while True:
        node = str(input('Enter Node : '))
        if node == 'x':
            break
        root = insert(root, int(node))
    
    while True:
        print("\n\n\
        Binary Search Tree Operations\n\
        -----------------------------\n\
        1. In-order Traversal\n\
        2. Pre-order Traversal\n\
        3. Post-order Traversal\n\
        4. Exit\n")
        choice = int(input("Enter your choice: "))
        switch = {
            1: lambda: inorder(root),
            2: lambda: preorder(root),
            3: lambda: postorder(root),
            4: exit,
        }
        func = switch.get(choice, lambda: print("Please enter a valid choice"))
        func()
