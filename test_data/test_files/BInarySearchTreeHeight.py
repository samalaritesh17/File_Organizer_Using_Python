#Height and depth of the BST are always same.
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
                
    def preorder(self):
        root = self
        print(root.key,end = " ")
        if(self.left is not None):
            self.left.preorder()
        if(self.right is not None):
            self.right.preorder()
            
    def height(self,root):#for depth also same logic
        if(root is None):
            return(-1)
        return(max(self.height(root.left),self.height(root.right))+1)
root1 = BST(120)       
lst = [100,20,10,222,200,240,333]

for i in lst:
    root1.insert(i)
print("pre order of the BST is : ")
root1.preorder()
print("\n")
print("height of the BST is : ")
print(root1.height(root1))
