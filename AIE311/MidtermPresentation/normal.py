class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, current, key):
        if current is None:
            return current

        if key < current.val:
            current.left = self._delete(current.left, key)
        elif key > current.val:
            current.right = self._delete(current.right, key)
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children: Get the inorder successor
            temp = self._minValueNode(current.right)
            current.val = temp.val
            current.right = self._delete(current.right, temp.val)

        return current

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Traversals
    def prefix(self, node):
        if node:
            print(node.val, end=" ")
            self.prefix(node.left)
            self.prefix(node.right)

    def infix(self, node):
        if node:
            self.infix(node.left)
            print(node.val, end=" ")
            self.infix(node.right)

    def postfix(self, node):
        if node:
            self.postfix(node.left)
            self.postfix(node.right)
            print(node.val, end=" ")

# ฟังก์ชันหลักสำหรับการ insert และ delete ตาม input list
def process_tree(insert_list, delete_list):
    tree = BinaryTree()
    
    # Insert nodes
    for key in insert_list:
        tree.insert(key)
    
    # Delete nodes
    for key in delete_list:
        tree.delete(key)
    
    # แสดงผลการ Traversal
    print("Prefix Traversal:")
    tree.prefix(tree.root)
    print("\nInfix Traversal:")
    tree.infix(tree.root)
    print("\nPostfix Traversal:")
    tree.postfix(tree.root)

# รับ Input list สำหรับ insert และ delete
insert_list = [50, 30, 20, 40, 70, 60, 80]
delete_list = [20, 30, 50]

process_tree(insert_list, delete_list)
