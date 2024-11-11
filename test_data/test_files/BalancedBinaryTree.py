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
    def height(self,root):#for depth also same logic
        if(root is None):
            return(-1)
        return(max(self.height(root.left),self.height(root.right))+1)
                
    def isBalanced(self,root):
        if(root is None):
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if(abs(lh - rh) > 1):
            return False
        return(self.isBalanced(root.left) and self.isBalanced(root.right))
        
        
        
root = BST(40)       
lst = [10,44,5,22,42,50]
for i in lst:
    root.insert(i)
res = root.isBalanced(root)
if(res == True):
    print("Balanced Binary Tree")
else:
    print("Not Balanced Binary Tree")
