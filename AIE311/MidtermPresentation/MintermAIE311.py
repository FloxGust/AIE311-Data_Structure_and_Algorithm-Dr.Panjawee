import graphviz

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
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            temp = self._minValueNode(current.right)
            current.val = temp.val
            current.right = self._delete(current.right, temp.val)

        return current

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def prefix(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.prefix(node.left, result)
            self.prefix(node.right, result)
        return result

    def infix(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.infix(node.left, result)
            result.append(node.val)
            self.infix(node.right, result)
        return result

    def postfix(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postfix(node.left, result)
            self.postfix(node.right, result)
            result.append(node.val)
        return result
    
    
    #Graphviz
    def visualize(self, filename="binary_tree"):
        dot = graphviz.Digraph()

        def add_nodes_edges(node):
            
            if node:
                dot.node(str(node.val))
                if node.left:
                    dot.edge(str(node.val), str(node.left.val))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(node.val), str(node.right.val))
                    add_nodes_edges(node.right)

        #Save file as png of insert and delete
        add_nodes_edges(self.root)
        dot.render(filename, format='png', cleanup=True)
        print(f"Saved as '{filename}.png'")


#Graphviz
def process_tree(insert_list, delete_list):
    tree = BinaryTree()
    
    for key in insert_list:
        tree.insert(key)
    
    print("\nTraversal after insert:")
    print("Prefix:", tree.prefix(tree.root))
    print("Infix:", tree.infix(tree.root))
    print("Postfix:", tree.postfix(tree.root))
    tree.visualize("insert")


    for key in delete_list:
        tree.delete(key)

    print("\nTraversal after delete:")
    print("Prefix:", tree.prefix(tree.root))
    print("Infix:", tree.infix(tree.root))
    print("Postfix:", tree.postfix(tree.root))
    tree.visualize("delete")
    

# insert_list = [50, 30, 20, 40, 70, 60, 80, 90, 100, 120, 33 ,75, 110, 95, 121]
# delete_list = [50]



insert_list = []
delete_list = [] 
mode = " "

while mode != 'exit':
    mode = input("Select mode: ")
    if mode == 'insert' or mode =='ins':
        insert_var = [int(x) for x in input("Enter insert multiple value: ").split(" ")]
        insert_list += insert_var 
    elif mode == 'delete'or mode =='del':
        delete_list = [int(x) for x in input("Enter delete multiple value: ").split(" ")]

    process_tree(insert_list, delete_list)

