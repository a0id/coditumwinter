from searchTree import BST
from time import sleep

tree = BST()

tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.printH()

tree.remove(5)

sleep(3)
tree.printH()