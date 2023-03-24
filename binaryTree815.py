#node class
class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None    #left side child
        self.right = None   #right side child

#binary tree class
class binaryTree:
    def __init__(self):
        self.root = None

    #insert function
    def insert(self, value):
        if self.root == None:   #at the very beginning root is null
            self.root = node(value)
        else:
            self._insert(value, self.root)  #if root exists then moves to recursive function 

    #recursive insert function
    def _insert(self, value, currentNode):
        if value < currentNode.value:   #for left children
            if currentNode.left == None:    #if left child does not exisit
                currentNode.left = node(value)
            else:
                self._insert(value, currentNode.left)   #recursive to find best place
        else:   #for right children
            if currentNode.right == None:   #if right child does not exisit
                currentNode.right = node(value)
            else:
                self._insert(value, currentNode.right)  #recursive to find best place

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

    #display function    
    def display(self):
        if self.root != None:
            self._display(self.root) #if root is not null then moves to recursive function

    #recursive display function
    def _display(self, currentNode):
        if currentNode != None:
            self._display(currentNode.left) #make left child as current node
            print (currentNode.value)   #display node value
            self._display(currentNode.right) #make right child chils as current node   

#testing
bt = binaryTree()   #object creation
#inserting values 
bt.insert(27)
bt.insert(13)
bt.insert(30)
bt.insert(81)
bt.insert(48)
bt.insert(92)
bt.insert(79)
bt.insert(19)
bt.insert(6)
bt.insert(68)
print("---Sorted values---")
#display values
bt.display()
#searching a value
print("---Searching values 48 and 12---")
print (bt.search(48))
print (bt.search(12))
