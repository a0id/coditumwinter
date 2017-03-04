from searchTree import BST
import os
from time import sleep
tree = BST()


tree.insert(10)
tree.insert(15)
tree.insert(3)
tree.insert(5)
tree.insert(2)
tree.insert(6)
tree.insert(14)
tree.printH()

sleep(5)

tree.remove(5)
tree.printH()