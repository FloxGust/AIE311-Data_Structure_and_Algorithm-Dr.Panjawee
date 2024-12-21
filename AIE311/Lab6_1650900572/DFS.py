class Node:
   
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left == None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right == None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

    def Print_inorder(self):
      if self.left:
         self.left.Print_inorder()
      print(self.data)
      if self.right:
         self.right.Print_inorder()

    def DFS_Search(self, val):
       
        if val == self.data:
            result = str(val) + " is found in the BST"
            return result
        
        elif val < self.data:
            
            if self.left:
                return self.left.DFS_Search(val)
            else:
                result = str(val) + " is not found in the BST"
                return result
        else:
            if self.right:
                return self.right.DFS_Search(val)
            else:
                result = str(val) + " is not found in the BST" 
                return result 

data = [53, 27, 84, 12, 91, 6, 35, 45, 78, 23, 69, 2, 39, 74, 18]

for i in range(len(data)):
   if i == 0:
      tree = Node(data[i])
   else:
      tree.insert(data[i])

print(tree.DFS_Search(20))
