from distutils.tests import here
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
class BST:
    def __init__(self):
        self.head = None
        self.counter = None
    def insertR(self, value, node):
        if value > node.data:
            if node.right == None:
                newNode = Node()
                newNode.data = value
                node.right = newNode
            else:
                self.insertR(value, node.right)
        else:
            if value < node.data:
                if node.left == None:
                    newNode = Node()
                    newNode.data = value
                    node.left = newNode
                else:
                    self.insertR(value, node.left)
    def insert(self, value):
        if self.head == None:
            newNode =  Node()
            newNode.data = value
            self.head = newNode
        else:
            self.insertR(value, self.head)
    def printerR(self, curr):
        if curr.left != None:
            self.printerR(curr.left)
        print(curr.data)
        if curr.right != None:
            self.printerR(curr.right)
    def printer(self):
        if self.head == None:
            print("Nothing in Tree!")
        else:
            self.printerR(self.head)
    def searchR(self, value, node):
        if node == None:
            return False
        elif value == node.data:
            return True
        elif value < node.data:
            return self.searchR(value, node.left)
        elif value > node.data:
            return self.searchR(value, node.right)
    def search(self, value):
        return self.searchR(value, self.head)
    def printHR(self, node, tab):
        if node.right != None:
            self.printHR(node.right, tab+1)
        for x in range(tab):
            print("\t", end="")
        print(node.data)
        if node.left != None:
            self.printHR(node.left, tab+1)
    def printH(self):
        if self.head == None:
            print("Nothing in Tree!")
        else:
            self.printHR(self.head, 0)
            
    def removeR(self, value, node):
        if node.data == value:
            if node.left == None and node.right == None: # Case One: Leaf
                return None
            elif node.left != None or node.right != None: # Case Two: One child
                if node.left:
                    return node.left
                else:
                    return node.right
            elif node.left != None and node.right != None: # Case Three: Two Children
                if node.right != None:
                    switchMe = node.data
                while True:
                    if node.left != None:
                        tempNode = node.left.data
                self.removeR(switchMe, self.head)
                
        elif value > node.data: # If it is to the right
            node.right = self.removeR(value, node.right)
            return node
        elif value < node.data: # If it is to the left
            node.left = self.removeR(value, node.left)
            return node
    def remove(self, value):
        self.removeR(value, self.head)