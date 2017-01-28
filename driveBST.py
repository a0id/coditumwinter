from searchTree import BST
from time import sleep
tree = BST()


tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.insert(4)
"""
tree.insert(3)
tree.insert(20)
tree.printH()
tree.remove(20)
"""
tree.printH()
tree.remove(4)

sleep(3)
tree.printH()