class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next
    
    #insertion into Double linked list
    def insertelement(self,value,loc):
        if self.head is None:
            print("Linked list is empty")
        else:
            newnode = Node(value)
            if(loc == 0):
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif(loc == 1):
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                temp = self.head
                index= 0
                while(index<loc-1):
                    temp = temp.next
                    index+=1
                newnode.next = temp.next
                newnode.prev = temp
                newnode.next.prev = newnode
                temp.next = newnode


    def insertbeforeposition(self, value, position):
        if self.head is None:
            print("Linked list is empty")
            return

        if position <= 0:
            new_node = Node(value)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            index = 1
            while temp and index < position:
                temp = temp.next
                index += 1

            if temp:
                new_node = Node(value)
                new_node.prev = temp.prev
                new_node.next = temp
                if temp.prev:
                    temp.prev.next = new_node
                temp.prev = new_node
            else:
                print("Position is out of range")
            
    def traverseDLL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            currnode = self.head
            while currnode:
                print(currnode.value,end="-->")
                currnode = currnode.next
    def reversetraversalDLL(self):
        if self.tail is None:
            print("The linked list is empty")
        else:
            currnode = self.tail
            while currnode:
                print(currnode.value,end="-->")
                currnode = currnode.prev
    def searchelement(self,key):
        if self.head is None:
            print("The linked list is empty")
        else:
            currnode = self.head
            index = 0 
            while currnode:
                index+=1
                if currnode.value == key:
                    print("element found at position : ",index)
                    break
                currnode = currnode.next
    #creation of double linked list
    def createDLL(self,value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        print("The DLL is created successfully...")
        
    def deleteelement(self,loc):
        if self.head is None:
            print("The list is empty")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif(loc == 1):
                self.tail = self.tail.prev
                self.tail.prev = None
                self.tail.next = None
            else:
                currnode = self.head
                if self.head is None:
                    print("There are no elements in the list")
                else:
                    currnode = self.head
                    index = 1
                    while(index<loc-1):
                        currnode = currnode.next
                        index+=1
                    currnode.next = currnode.next.next
                    currnode.next.prev = currnode
            print("deletion successful")  
    
    def deleteentireDLL(self):
        self.head = None
        self.tail = None 
        print("Entire DLL is deleted...")
        
double = Doublelinkedlist()
print([node.value for node in double])
double.createDLL(120)
double.insertelement(122,1)
double.insertelement(12,1)
double.insertelement(112,1)
double.insertelement(1222,1)
double.insertelement(1332,1)
print([node.value for node in double])
# double.insertbeforeposition(1234,10)
# print([node.value for node in double])
#double.traverseDLL()
# print("\n")
# double.reversetraversalDLL()
# print("\n")
# double.searchelement(120)
double.deleteelement(3)
print([node.value for node in double])
double.deleteentireDLL()
print([node.value for node in double])

        
