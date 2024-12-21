class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)
      if self.left != None or self.right != None:
         print('->',end="")

root = Node(10)
root.PrintTree()