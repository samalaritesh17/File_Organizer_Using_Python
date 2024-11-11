class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
    def insert(self,data):
        if(self.key is None):
            self.key = data
            return
        if(self.key == data):
            return
        if(data < self.key):
            if(self.left is not None):
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if(self.right is not None):
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self,data):
        if(self.key == data):
            print("Node is found...")
            return
        if(data < self.key):
            if(self.left is not None):
                self.left.search(data)
            else:
                print("Node is not found...")
        else:
            if(self.right is not None):
                self.right.search(data)
            else:
                print("Node is not found...")    

    def min_node(self):
        current = self
        while(current.left is not None):
            current = current.left
        print(current.key)
        
    def max_node(self):
        current = self
        while(current.right is not None):
            current = current.right
        print(current.key)

    def preorder(self):
        print(self.key,end = " ")
        if(self.left is not None):
            self.left.preorder()
        if(self.right is not None):
            self.right.preorder()   
             
    def postorder(self):
        if(self.left is not None):
            self.left.postorder()
        if(self.right is not None):
            self.right.postorder()
        print(self.key,end = " ")
        
    def inorder(self):
        if(self.left is not None):
            self.left.inorder()
        print(self.key,end = " ")
        if(self.right is not None):
            self.right.inorder()
    
    def LevelOrderTraversal(self):
        queue = []
        queue.append(self)
        while(len(queue) != 0):
            node = queue.pop(0)
            print(node.key,end = " ")
            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)
    
    def delete(self,data):
        if(self.key is None):
            print("Tree is Empty...")
            return
        if(data < self.key):
            if(self.left is not None):
                self.left = self.left.delete(data)
            else:
                print("Node is not found to perform deletion...")
        elif(data > self.key):
            if(self.right is not None):
                self.right = self.right.delete(data)
            else:
                print("Node is not found to perform deletion...")
        else:
            if(self.left is None):
                temp = self.right
                self = None
                return temp
            if(self.right is None):
                temp = self.left
                self = None
                return temp
            node = self.right # replace the deleted node with smallest value in RST
            while(node.left is not None):
                node = node.left
            self.key = node.key
            self.right = self.right.delete(data)
        return self
root = BST(None)
while(True):
    print("\nMenu\n1.insert\n2.search\n3.preorder\n4.inorder\n5.postorder\n6.delete\n7.minimum_node\n8.maximum_node\n9LevelOrderTraversal\n")
    print("What would you like to perform : ")
    input1 = int(input())
    if(input1 == 1):
        size = int(input("Enter the size of the list : "))
        print("Enter the elements to insert into the tree: ")
        lst = list(map(int,input().split()))
        for i in lst:
            root.insert(i)
        print("elements inserted successfully...")
        print("\n")
    elif(input1 == 2):
        ele = int(input("Enter the element you want to search : "))
        root.search(ele)
        print("search operation performed succesfully...")
        print("\n")
    elif(input1 == 3):
        print("The preorder traversal of the tree is : ")
        root.preorder()
        print("\n")
    elif(input1 == 4):
        print("The inorder traversal of the tree is : ")
        root.inorder()
        print("\n")
    elif(input1 == 5):
        print("The postorder traversal of the tree is : ")
        root.postorder()
        print("\n")
    elif(input1 == 6):
        ele = int(input("Enter the element you want to delete : "))
        root.delete(ele)
        print("deletion performed successfully...")
        print("\n")
    elif(input1 == 7):
        print("The minimum node in the BST is : ")
        root.min_node()
    elif(input1 == 8):
        print("The maximum node in the BST is : ")
        root.max_node()
    elif(input1 == 9):
        print("The Level Order traversal of the tree is : ")
        root.LevelOrderTraversal()
    else:
        print("Please enter the number in range of (1-9) only!!!")
        print("\n")
        break
    


