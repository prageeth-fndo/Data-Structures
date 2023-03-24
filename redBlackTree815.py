#node class
class node:    
    def __init__(self,value = None):
        self.value = value
        self.red = False    #black = True and red = False
        self.parent = None
        self.left = None
        self.right = None

#red-black binary tree class
class redBlackTree:    
    def __init__(self):
        self.root = None
        self.size =0

    #insert function
    def insert(self,value,currentNode = None):        
        self.size += 1
        newNode = node(value)        
        if self.root == None:   #if nothing in the tree
            newNode.red = False
            self.root = newNode
            return  #if condition ends here
        
        currentNode = self.root     #finding the correct place for newNode
        while currentNode != None:
            parent = currentNode
            if newNode.value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        newNode.parent = parent    #assign parents and siblings to the new node
        if newNode.value < newNode.parent.value:
            newNode.parent.left = newNode
        else:
            newNode.parent.right = newNode
            
        self.balancingTree(newNode) #balancing the tree after inserting

    #search function
    def search(self, value):
        if self.root != None:   #if root exists then moves to recursive function
            return self._search(value, self.root)
        else:
            return False    #if root is null then return 'false'

    #recursive search function
    def _search (self, value, currentNode):
        if value == currentNode.value: #check searching value with 'current node'
            return True
        elif value < currentNode.value and currentNode.left != None:    #check searching value is less than 'current node'
            return self._search(value, currentNode.left) #recursive with left child as current node
        elif value > currentNode.value and currentNode.right != None:   #check searching value is greater than 'current node'
            return self._search(value, currentNode.right)   #recursive right child as current node
        return False #if no search found

    #after insertion tree fixing function to balance the tree
    def balancingTree(self,newNode):               
        while newNode.parent.red == True and newNode != self.root:
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                if uncle.red:   #applying rb rule number 3                    
                    newNode.parent.red = False
                    uncle.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.right:     #if newNode is inside grandchild                        
                        newNode = newNode.parent
                        self.leftRotate(newNode)   #parent left rotating
                    #if newNode is outside grandchild
                    newNode.parent.red = False
                    newNode.parent.parent.red = True    #applying rb rule number 3
                    self.rightRotate(newNode.parent.parent)    #grand parent right rotating
            else:
                uncle = newNode.parent.parent.left
                if uncle.red:   #applying rb rule number 3                    
                    newNode.parent.red = False
                    uncle.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.left:      #if newNode is inside grandchild
                        newNode = newNode.parent
                        self.rightRotate(newNode)      #parent right rotation
                    #if newNode is outside grandchild
                    newNode.parent.red = False
                    newNode.parent.parent.red = True    #applying rb rule number 3
                    self.leftRotate(newNode.parent.parent)     #grand parent left rotating
        self.root.red = False   #applying rule number 2
    
    def leftRotate(self,newNode):        
        print("Rotating left")

        sibling = newNode.right
        newNode.right = sibling.left
        
        if sibling.left != None:    #turning sibling's left subtree into node's right subtree
            sibling.left.parent = newNode
        sibling.parent = newNode.parent
        if newNode.parent == None:
            self.root = sibling
        else:
            if newNode == newNode.parent.left:
                newNode.parent.left = sibling
            else:
                newNode.parent.right = sibling
        sibling.left = newNode
        newNode.parent = sibling

    def rightRotate(self,newNode):        
        print("Rotating right")
        
        sibling = newNode.left
        newNode.right = sibling.right
        
        if sibling.right != None:   #turning sibling's left subtree into node's right subtree
            sibling.right.parent = newNode
        sibling.parent = newNode.parent
        if newNode.parent == None:
            self.root = sibling
        else:
            if newNode == newNode.parent.right:
                newNode.parent.right = sibling
            else:
                newNode.parent.left = sibling
        sibling.right = newNode
        newNode.parent = sibling

    #checking node is red
    def is_red(self):        
        return self.root != None and self.root.red == 1;

    #checking node is black
    def is_black(self):
        return self.root != None and self.root.black == 1;

    #display function
    def display(self):
        if self.root != None:
            self._display(self.root)    #if root is not null then moves to recursive function

    #recursive display function
    def _display(self, currentNode):
        if currentNode != None:
            self._display(currentNode.left)     #make left child as current node
            print (currentNode.value)       #display node value
            self._display(currentNode.right)    #make right child chils as current node

#testing
rbt = redBlackTree()
#inserting
rbt.insert(452)
rbt.insert(264)
rbt.insert(820)
rbt.insert(651)
rbt.insert(546)
rbt.insert(315)
rbt.insert(566)
rbt.insert(731)
rbt.insert(148)
rbt.insert(365)
#displaying
print("---Sorted values---")
rbt.display()
#searching
print("---Searching values 315 and 845---")
print(rbt.search(315))
print(rbt.search(845))

